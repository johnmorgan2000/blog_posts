from django.test import TestCase
from django.urls import reverse

# Create your tests here.


#Ginger Keys Addition
class TestHomeView(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
