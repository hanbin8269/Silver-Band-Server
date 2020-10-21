from django.test import TestCase, Client
from rest_framework import status
import unittest
from .models import User
import json

client = Client()


class SignUp(TestCase):
    def setUp(self):
        User.objects.create(
            username="hanbin",
            email="gksqls0128@gmail.com",
            password="0128gksqls",
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_signup_success(self):
        user = {
            "username": "habi",
            "email": "gkql0128@gmail.com",
            "password": "0128gksqls",
        }

        response = client.post(
            "/users/auth/register/", json.dumps(user), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_exist_email(self):
        user = {
            "username": "hanbin",
            "email": "gksqls0128@gmail.com",
            "password": "0128gksqls",
        }
        response = client.post(
            "/users/auth/register/", json.dumps(user), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content.decode()),
            {"email": ["user with this email address already exists."]},
        )


class Login(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "hanbin",
            "email": "gksqls0128@gmail.com",
            "password": "0128gksqls",
        }
        User.objects.create_user(**self.credentials)

    def tearDown(self):
        User.objects.all().delete()

    def test_login_success(self):
        response = client.post(
            "/users/auth/login/", self.credentials, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_not_exit_account(self):
        fake_credentials = {
            "username": "hanbin",
            "email": "gksqls@gmail.com",
            "password": "0128gksqls",
        }
        response = client.post(
            "/users/auth/login/", fake_credentials, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)