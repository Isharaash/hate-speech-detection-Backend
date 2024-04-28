import unittest
import requests

class TestHatePredictionAPI(unittest.TestCase):

    def setUp(self):
       
        self.base_url = 'http://localhost:5000/api'
        self.headers = {'Content-Type': 'application/json'}



    def test_register(self):
       
        payload = {
            "firstName": "Test",
            "lastName": "User",
            "email": "testaa@gmail.com",
            "password": "123"
        }
        response = requests.post(f'{self.base_url}/register', json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)




    def test_login(self):
        
        payload = {
            "email": "testaa@gmail.com",
            "password": "123"
        }
        response = requests.post(f'{self.base_url}/login', json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)

    

    def tearDown(self):
     
        pass

if __name__ == '__main__':
    unittest.main()
