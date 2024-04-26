import unittest
from app import app


class TestApp(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def test_register_endpoint(self):
        # Test registration endpoint
        data = {
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john522@example.com',
            'password': 'password123'
        }
        response = self.app.post('/api/register', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful', response.data)
    
    def test_login_endpoint(self):
        # Test login endpoint
        data = {
            'email': 'user@gmail.com',
            'password': '1234'
        }
        response = self.app.post('/api/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)
    
    def test_predict_endpoint(self):
        # Test prediction endpoint
        data = {
            'text': 'Love.'
        }
        # Assuming the user is logged in, set session
        with self.app.session_transaction() as sess:
            sess['user_id'] = 7
        response = self.app.post('/api/post', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No hate', response.data)  # Assuming prediction is 'No hate'
    
    def test_view_post_endpoint(self):
        # Test view post endpoint
        # Assuming the user is logged in, set session
        with self.app.session_transaction() as sess:
            sess['user_id'] = 7
        response = self.app.get('/api/view_post')
        self.assertEqual(response.status_code, 200)
        # Add more assertions as per the response structure
    
    def test_delete_post_endpoint(self):
        # Test delete post endpoint
        # Assuming the user is logged in, set session
        with self.app.session_transaction() as sess:
            sess['user_id'] = 7
        # Assuming prediction_id exists and belongs to the logged-in user
        response = self.app.delete('/api/delete_post/99')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prediction deleted successfully', response.data)
    
    def test_get_total_users_endpoint(self):
        # Test get total users endpoint
        # Assuming the user is logged in, set session
        with self.app.session_transaction() as sess:
            sess['user_id'] = 6
        response = self.app.get('/api/admin/total_users')
        self.assertEqual(response.status_code, 200)
        # Add more assertions as per the response structure


if __name__ == '__main__':
    unittest.main()
