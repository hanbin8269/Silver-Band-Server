from django.test import TestCase, Client
from rest_framework import status
from .models import Location
# Create your tests here.

client = Client()

class CreateLocation(TestCase):
    
    def test_create_sucess(self):
        location = {
            "wearer_id" : 0,
            "x" : 35.044515, 
            "y" : 126.718850,
            "created_At" : "2020-10-27 15:57:23" # %Y-%m-%d %H:%M:%S
        }

        response = client.post(
            "/gps/", location, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_fail_with_not_exist_wearer(self):
        location = {
            "wearer_id" : 1234,
            "x" : 35.044515, 
            "y" : 126.718850,
            "created_At" : "2020-10-27 15:57:23" # %Y-%m-%d %H:%M:%S 
        }

        response = client.post(
            "/gps/", location, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)