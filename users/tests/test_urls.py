import django
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from users import views as users_views
from django.contrib.auth import views as auth_views

class TestUrls(SimpleTestCase):
    def test_home_view(self):
        '''
        1. Test that name of the home path (home) resolves to the home view (users_views.home)
        '''
        url = reverse('home') # takes in the name of the path as an argument
        # the reverse() is similar to the url template tag in your code
        # print(resolve(url)) # returns ResolverMatch object that allows you to access various metadata about the resolved url
        # ResolverMatch(func=users.views.home, args=(), kwargs={}, url_name='home', app_names=[], namespaces=[], route='')
        # func is the view function that would be used to serve the url
        # args is the arguments that would be passed to the view function as parsed from the url
        # kwargs is the keyword arguments that would be passed to the view function as parsed from th url
        # others are url_name, route, tried, app_name, app_names, namespace, namespaces, view_name
        self.assertEquals(resolve(url).func, users_views.home)

    def test_login_view(self):
        url = reverse('login')
        # the login path uses a class-based view - this is how you test it
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_view(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_register_view(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, users_views.register)

    def test_post_view(self):
        url = reverse('post')
        self.assertEquals(resolve(url).func, users_views.post)

    def test_delete_post(self):
        url = reverse('delete-post', kwargs={'post_id': 1})
        self.assertEquals(resolve(url).func, users_views.delete_post)