from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from PrinterQueue.api.models import User
from rest_framework.test import APIClient


class UserTests(APITestCase):
    def setUp(self):
        # Make all requests in the context of a logged in session.
        self.client = APIClient()
        self.client.login(username='admin', password='password123')

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = 'http://127.0.0.1:8000/users/'
        data = {'username': 'jmahe', 'email': 'jmachairas@umassd.edu'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class JobTests(APITestCase):
    def setUp(self):
        # Make all requests in the context of a logged in session.
        self.client = APIClient()
        self.client.login(username='admin', password='password123')

    def test_create_job(self):
        """
        Ensure we can create a new user object.
        """
        url = 'http://127.0.0.1:8000/jobs/'
        data = {'jobname': 'jobx', 'jobid': 10, 'description': 'blah', 'orientation': 'landscape', 'priority': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PrinterTests(APITestCase):
    def setUp(self):
        # Make all requests in the context of a logged in session.
        self.client = APIClient()
        self.client.login(username='admin', password='password123')

    def test_create_printer(self):
        """
        Ensure we can create a new user object.
        """
        url = 'http://127.0.0.1:8000/printers/'
        data = {'devicename': 'printerx', 'deviceid': 10, 'description': 'blah', 'copies': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

