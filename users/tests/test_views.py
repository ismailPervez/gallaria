from pydoc import resolve
from django.test import TestCase, Client
from django.urls import reverse
from users import views
from users.models import Post
from django.contrib.auth.models import User

'''
The test client is a python class that acts as a dummy web browser allowing you to test your views and interact with your web app programatically.

With this you can:
1. Simulate a GET and POST request and observe the response
2. See the chain of redirects (if any) and check url status code at each step
3. Test that a given request is rendered by a django template, with a template contexts that contains certain values
'''

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # A User object to test login functionality
        self.credentials = {
            'username': 'test_dummy',
            'password': 'testing12345'
        }
        User.objects.create_user(**self.credentials)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')

    def test_login_view(self):
        # testing the get request
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        # test the post request
        # senf login data
        response = self.client.post(reverse('login'), self.credentials, follow=True)
        # user should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)

    