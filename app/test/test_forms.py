from django.test import TestCase
from app.forms import CreateBlogForm


class TestCreateBlogForm(TestCase):
    def test_form_is_valid(self):
        form = CreateBlogForm({
            'title': 'Test Case',
            'author': 'John Morgan',
            'body': 'Running a Test',
            'cover_image_url': 'Test.com'
        })

        is_valid = form.is_valid()

        self.assertTrue(is_valid)

    def test_form_is_invalid_with_empty_title(self):
        form = CreateBlogForm({
            'title': '   ',
            'author': 'John Morgan',
            'body': 'Running a Test',
            'cover_image_url': 'Test.com'
        })

        is_valid = form.is_valid()

        self.assertFalse(is_valid)

    def test_form_is_invalid_with_empty_author(self):
        form = CreateBlogForm({
            'title': 'Test Case',
            'author': '',
            'body': 'Running a Test',
            'cover_image_url': 'Test.com'
        })

        is_valid = form.is_valid()

        self.assertFalse(is_valid)

    def test_form_is_invalid_with_empty_body(self):
        form = CreateBlogForm({
            'title': 'Test Case',
            'author': 'John Morgan',
            'body': '  ',
            'cover_image_url': 'Test.com'
        })

        is_valid = form.is_valid()

        self.assertFalse(is_valid)

    def test_form_is_invalid_with_empty_body(self):
        form = CreateBlogForm({
            'title': 'Test Case',
            'author': 'John Morgan',
            'body': '  ',
            'cover_image_url': 'Test.com'
        })

        is_valid = form.is_valid()

        self.assertFalse(is_valid)
