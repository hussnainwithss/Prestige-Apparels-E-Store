from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import login,logout,signup
# from django.contrib.admin.site import AdminSite

# Create your tests here.

class TestUrls(TestCase):
    
    def test_login_url_resolves(self):
        print("Testing resolution of Login URL")
        # getting corresponding url by name of url 
        # login_system is the namespace 
        # login is name of the url 
        url = reverse('login_system:login')  
        # resolving the URL path to corresponding view function
        # asserting that the resolved url view and view defined in  
        # url.py for login are equal
        self.assertEquals(resolve(url).func,login)
       
    def test_signup_url_resolves(self):
        print("\nTesting resolution of Signup URL")
        # getting corresponding url by name of url 
        # login_system is the namespace 
        # login is name of the url 
        url = reverse('login_system:signup')
        # resolving the URL path to corresponding view function
        # asserting that the resolved url view and view defined in  
        # url.py for login are equal
        self.assertEquals(resolve(url).func,signup)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        
    
    def test_login_view_GET(self):
        print("\nTesting Login view GET request and template fetching")
        response = self.client.get(reverse('login_system:login'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')


    def test_signup_view_GET(self):
        print("\nTesting Signup view GET request and template fetching")
        response = self.client.get(reverse('login_system:signup'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'signup.html')

    
    
