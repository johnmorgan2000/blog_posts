from django.test import TestCase
from app import models


class TestBlogPost(TestCase):
    def test_get_blogs(self):

        john = models.BlogPost(
            title='test',
            body='this is a test case. yay.',
            author='John',
            cover_image_url='me.org')
        john.save()

        self.assertQuerysetEqual(
            qs=models.BlogPost.get_blogs(),
            values=['John'],
            transform=lambda blogpost: blogpost.author)
