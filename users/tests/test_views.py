from pydoc import resolve
from django.test import TestCase, Client
from django.urls import reverse
from users import views
from users.models import Post
from django.contrib.auth.models import User
from cloudinary import CloudinaryImage

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
        self.user = User.objects.create_user(**self.credentials)
        # A Post object to test post functionality
        file = CloudinaryImage("picture.png")
        self.post = Post.objects.create(picture=file, user=self.user)

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

    def test_post_view(self):
        '''
        This view is only accessible by logged in users,
        therefore, you need to login first before request this view otherwise it will just redirect to the login view returning a status code of 302 (Found redirect status response code)
        When you apply a kwarg of follow=True, you will get a 200 status code, but it would have redirected to login.html so the template used will be for login.
        to login, use client.login(username='', password='')
        '''
        # GET request
        self.client.login(**self.credentials)
        response = self.client.get(reverse('post'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/post.html')
        # POST request
        response = self.client.post(reverse('post'), {'post': self.post})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/post.html')
        '''
        NOTE: from the above test we find that the we can create a post without having the caption, since the caption column is nullable (null not specified)
        '''

'''
NOTE: using reverse() when referring to a url makes the tests more portable because if you change your url scheme, your tests will still work
'''