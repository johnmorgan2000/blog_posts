from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

# Create your tests here.


#Ginger Keys Addition
class TestHomeView(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    @patch('app.models.BlogPost.get_blogs')
    def test_home_gets_blogs(self, get_blogs):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.context['blog_posts'],
                         get_blogs.return_value)
