import unittest
import requests

class TestAppIntegration(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations
        self.base_url = "http://localhost:5000/api/"
        
        
    def test_register(self):
        # Test registration functionality
        register_url = self.base_url + "register"
        register_data = {
            "firstName": "John",
            "lastName": "Doe",
            "email": "ashen2@gmail.com",
            "password": "password",
            "userType": "USER"
        }
        response = requests.post(register_url, json=register_data)
        
        # Assert that registration was successful and the correct response is received
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())  
        
        
        

    def test_login(self):
        # Test login functionality
        login_url = self.base_url + "login"
        login_data = {
            "email": "user@gmail.com",
            "password": "1234"
        }
        response = requests.post(login_url, json=login_data)
        
        # Assert that login was successful and the correct response is received
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertIn("id", response.json())
        self.assertIn("firstName", response.json())
        self.assertIn("lastName", response.json())
        self.assertIn("userType", response.json())

    def test_prediction(self):
        # Test prediction functionality
        login_url = self.base_url + "login"
        login_data = {
            "email": "user@gmail.com",
            "password": "1234"
        }
        login_response = requests.post(login_url, json=login_data)
        
        # Extract user ID from login response
        user_id = login_response.json()["id"]

        prediction_url = self.base_url + "post"
        prediction_data = {
            "text": "This is a test prediction"
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        prediction_response = requests.post(prediction_url, json=prediction_data, headers=headers, cookies=login_response.cookies)
        
        # Assert that prediction was made successfully
        self.assertEqual(prediction_response.status_code, 200)
        self.assertIn("text", prediction_response.json())
        self.assertIn("prediction", prediction_response.json())
        self.assertIn("user_id", prediction_response.json())
        
    def test_view_post(self):
        # Test view_post functionality
        login_url = self.base_url + "login"
        login_data = {
            "email": "user@gmail.com",
            "password": "1234"
        }
        login_response = requests.post(login_url, json=login_data)
        
        # Extract user ID from login response
        user_id = login_response.json()["id"]

        view_post_url = self.base_url + "view_post"
        view_post_response = requests.get(view_post_url, cookies=login_response.cookies)
        
        # Assert that view_post request was successful
        self.assertEqual(view_post_response.status_code, 200)
        self.assertIn("predictions", view_post_response.json())
        
        
        
    def test_delete_post(self):
        # Test delete_post functionality
        login_url = self.base_url + "login"
        login_data = {
            "email": "user@gmail.com",
            "password": "1234"
        }
        login_response = requests.post(login_url, json=login_data)
        
        # Extract user ID from login response
        user_id = login_response.json()["id"]

        # Specify the prediction ID manually
        prediction_id = 115

        delete_post_url = self.base_url + f"delete_post/{prediction_id}"
        delete_post_response = requests.delete(delete_post_url, cookies=login_response.cookies)
        
        # Assert that delete_post request was successful
        self.assertEqual(delete_post_response.status_code, 200)
        self.assertIn("message", delete_post_response.json())
        
        
        
    def test_total_users(self):
        # Test total_users functionality
        login_url = self.base_url + "login"
        login_data = {
            "email": "admin@gmail.com",  # Assuming admin credentials
            "password": "1234"
        }
        login_response = requests.post(login_url, json=login_data)
        
        # Assert that login was successful and the correct response is received
        self.assertEqual(login_response.status_code, 200)

        # Get total users using the admin credentials
        total_users_url = self.base_url + "admin/total_users"
        total_users_response = requests.get(total_users_url, cookies=login_response.cookies)

        # Assert that total_users request was successful
        self.assertEqual(total_users_response.status_code, 200)
        self.assertIn("total_users", total_users_response.json())

    def tearDown(self):
        # Clean up any test data or configurations
        pass



    def tearDown(self):
        # Clean up any test data or configurations
        pass

if __name__ == "__main__":
    unittest.main()
