from flask import Flask, request, jsonify, session, redirect, url_for
import mysql.connector
import bcrypt
import pickle
import logging
from clean_text import clean_text
from sklearn.feature_extraction.text import CountVectorizer
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app, supports_credentials=True, methods=["GET", "POST", "DELETE"])

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hate"
)
cursor = db.cursor()

# Create a table to store predicted text and its prediction if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        text TEXT,
        prediction VARCHAR(255),
        user_id INT
    )
""")

# Load SVM model
with open('svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)

# Load CountVectorizer tokenizer
with open('count_vectorizer.pkl', 'rb') as f:
    count_vectorizer = pickle.load(f)


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    email = data.get('email')
    password = data.get('password')
    userType = data.get('userType', 'USER')

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    query = "INSERT INTO users (first_name, last_name, email, password, user_type) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (firstName, lastName, email, hashed_password, userType))
    db.commit()

    logging.info("User registered: {}".format(email))

    return jsonify({"message": "Registration successful"})




@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        cursor.execute("SELECT id, first_name, last_name, password, user_type FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]  # Set session after successful login
            logging.info("User logged in: {}".format(email))
            return jsonify({
                "message": "Login successful",
                "id": user[0],
                "firstName": user[1],
                "lastName": user[2],
                "userType": user[4]
            })
        else:
            logging.error("Failed login attempt: {}".format(email))
            return jsonify({"error": "Invalid email or password"}), 401
    except Exception as e:
        logging.error("Error during login: {}".format(str(e)))
        return jsonify({"error": "An unexpected error occurred"}), 500



@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    logging.info("User logged out")
    return jsonify({"message": "Logout successful"})

@app.route('/api/post', methods=['POST'])
def predict():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized access"}), 401

    data = request.get_json(force=True)
    text = data['text']
    user_id = session['user_id']
    cleaned_text = clean_text(text)
    vectorized_text = count_vectorizer.transform([cleaned_text])
    prediction = svm_model.predict(vectorized_text)[0]

    if prediction < 0.5:
        result = "No hate"
        prediction = int(prediction)
        cursor.execute("INSERT INTO predictions (text, prediction, user_id) VALUES (%s, %s, %s)", (text, prediction, user_id))
        db.commit()
        logging.info("Prediction saved for user {}: {}".format(user_id, result))
        return jsonify({"text": text, "prediction": result, "user_id": user_id})
    else:
        result = "Hate and abusive"
        # Don't save anything in the database
        return jsonify({"text": text,"prediction": result})


@app.route('/api/view_post', methods=['GET'])
def get_predictions():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized access"}), 401
    
    user_id = session['user_id']
    try:
        cursor.execute("SELECT id, text, prediction FROM predictions WHERE user_id = %s", (user_id,))
        predictions = cursor.fetchall()
        prediction_list = []
        for prediction in predictions:
            prediction_dict = {
                "id": prediction[0],
                "text": prediction[1],
                "prediction": "No hate" if prediction[2] < 0.5 else "Hate and abusive",
                "user_id": user_id
            }
            prediction_list.append(prediction_dict)
        
        return jsonify({"predictions": prediction_list})
    except Exception as e:
        logging.error("Error fetching predictions: {}".format(str(e)))
        return jsonify({"error": "An unexpected error occurred while fetching predictions"}), 500

@app.route('/api/delete_post/<int:prediction_id>', methods=['DELETE'])
def delete_prediction(prediction_id):
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized access"}), 401
    
    user_id = session['user_id']
    try:
        cursor.execute("SELECT id FROM predictions WHERE id = %s AND user_id = %s", (prediction_id, user_id))
        prediction = cursor.fetchone()
        if prediction:
            cursor.execute("DELETE FROM predictions WHERE id = %s", (prediction_id,))
            db.commit()
            logging.info("Prediction deleted for user {}: {}".format(user_id, prediction_id))
            return jsonify({"message": "Prediction deleted successfully"})
        else:
            return jsonify({"error": "Prediction not found or unauthorized access to delete"}), 404
    except Exception as e:
        logging.error("Error deleting prediction: {}".format(str(e)))
        return jsonify({"error": "An unexpected error occurred while deleting prediction"}), 500



@app.route('/api/admin/total_users', methods=['GET'])
def get_total_users():
    # Check if the user is authenticated
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized access"}), 401
    
    # Retrieve user information from session
    user_id = session['user_id']
    
    try:
        # Fetch total number of users excluding admins
        cursor.execute("SELECT COUNT(*) FROM users WHERE user_type = 'USER'")
        total_users = cursor.fetchone()[0]
            
        return jsonify({"total_users": total_users})
    except Exception as e:
        logging.error("Error fetching total users: {}".format(str(e)))
        return jsonify({"error": "An unexpected error occurred while fetching total users"}), 500

if __name__ == '__main__':
    # Run the Flask app using Gunicorn
    app.run(debug=False, host='0.0.0.0', port=5000)


