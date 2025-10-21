from rest_framework.test import APIClient
from django.test import TestCase


class BlogAPITest(TestCase):
    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)
        self.PATH = "/api/v1/posts/"
        self.data = {'id': 1, 'title': 'Test Title', 'content': 'This is a Test Content'}
        self.user = {'username': 'testboy', 'password': '0021Arko'}
        
    def test_authentication(self):
        self.assertEqual(self.user['username'], 'testboy')
        self.assertNotEqual(self.user['password'], '1234Uche')
        self.client.login()

    def test_create_post(self):
        self.client.post(path=self.PATH, data=self.data, format='json')

    def test_get_post_list(self):
        self.client.get(self.PATH)

    def test_logout(self):
        self.client.logout()

    # def test_get_post(self):
    #     self.client.get(self.PATH, query_params={'id': 100})


    

