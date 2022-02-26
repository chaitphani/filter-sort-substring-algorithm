from .models import UserData
from rest_framework.test import APITestCase
from django.urls import reverse
import mock



class UserDataTestCase(APITestCase):

    def test_get_list_a_user(self):
        url = reverse("users_data")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_get_should_fail_if_worng_method_called(self):
        url = reverse("users_data")
        response = self.client.post(url)
        self.assertEqual(400, response.status_code)

    def test_create_a_user(self):
        url = reverse("users_data")
        response = self.client.post(url, {
            "first_name": "Harish",
            "last_name":'krishna',
            "email":"harish@gmail.com",
            "company_name":"techm",
            "city":"hyderabad",
            "state":"telangana",
            "zip":12345,
            "web":"https://www.google.co.in",
            "age":78
        }, format='json')
        self.assertEqual(201, response.status_code)

    def test_create_a_user_with_existing_email(self):
        url = reverse("users_data")
        response1 = self.client.post(url, {
            "first_name": "Harish",
            "last_name":'krishna',
            "email":"harish@gmail.com",
            "company_name":"techm",
            "city":"hyderabad",
            "state":"telangana",
            "zip":12345,
            "web":"https://www.google.co.in",
            "age":78
        }, format='json')
        response = self.client.post(url, {
            "first_name": "Harish12",
            "last_name":'krishna12',
            "email":"harish@gmail.com",
            "company_name":"techmahindra",
            "city":"hyderabad",
            "state":"telangana",
            "zip":12345,
            "web":"https://www.google.co.in",
            "age":64
        }, format='json')
        self.assertEqual(400, response.status_code)

    def test_get_a_user_with_id(self):
        url = reverse("users_data")
        response = self.client.post(url, {
            "first_name": "Harish12",
            "last_name":'krishna12',
            "email":"harish@gmail.com",
            "company_name":"techmahindra",
            "city":"hyderabad",
            "state":"telangana",
            "zip":12345,
            "web":"https://www.google.co.in",
            "age":64
        }, format='json')
        url = 'http://localhost:8000/'+str(response.data['id'])+'/'
        response = self.client.get(url, format="json")
        self.assertEqual(200, response.status_code)        

    def test_update_a_user(self):
        url = reverse("users_data")
        response = self.client.post(url, {
            "first_name": "Harish12",
            "last_name":'krishna12',
            "email":"harish@gmail.com",
            "company_name":"techmahindra",
            "city":"hyderabad",
            "state":"telangana",
            "zip":12345,
            "web":"https://www.google.co.in",
            "age":64
        }, format='json')
        url = 'http://localhost:8000/'+str(response.data['id'])+'/'
        data = {'first_name':'harish1', 'last_name':'krishna1'}
        response = self.client.put(url, data=data, format="json")
        self.assertEqual(400, response.status_code)   

    def test_delete_a_user(self):
        url = reverse("users_data")
        response = self.client.post(url, {
            "first_name": "Harish12",
            "last_name":'krishna12',
            "email":"harish@gmail.com",
            "company_name":"techmahindra",
            "city":"hyderabad",
            "state":"telangana",
            "zip":12345,
            "web":"https://www.google.co.in",
            "age":64
        }, format='json')
        url = 'http://localhost:8000/'+str(response.data['id'])+'/'
        response = self.client.delete(url)
        self.assertEqual(204, response.status_code)
