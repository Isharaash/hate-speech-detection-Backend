import unittest
from app import app


class TestApp(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        
        
    
    def test_register_endpoint(self):
      
        data = {
            'firstName': 'Ashen',
            'lastName': 'Wegapitiya',
            'email': 'wegapitiya@gmail.com',
            'password': 'password123'
        }
        response = self.app.post('/api/register', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful', response.data)
    
    
    
    
    def test_login_endpoint(self):
      
        data = {
            'email': 'isharaashen1234@gmail.com',
            'password': '2000'
        }
        response = self.app.post('/api/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)
    
    
    
    
    
    def test_predict_endpoint(self):
        
        data = {
            'text': 'Love.'
        }
       
        with self.app.session_transaction() as sess:
            sess['user_id'] = 7
        response = self.app.post('/api/post', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No hate', response.data)  
    
    
    
    
    
    
    def test_view_post_endpoint(self):
       
        with self.app.session_transaction() as sess:
            sess['user_id'] = 7
        response = self.app.get('/api/view_post')
        self.assertEqual(response.status_code, 200)
       
    
    
    
    
    
    def test_delete_post_endpoint(self):
       
        with self.app.session_transaction() as sess:
            sess['user_id'] = 7
        
        response = self.app.delete('/api/delete_post/128')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prediction deleted successfully', response.data)
        
        
        
        
    
    def test_get_total_users_endpoint(self):
        
        with self.app.session_transaction() as sess:
            sess['user_id'] = 6
        response = self.app.get('/api/admin/total_users')
        self.assertEqual(response.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()
