from django.forms import Form
from django import forms
from app.validators import validate_not_empty


class CreateBlogForm(Form):
    title = forms.CharField(
        label="Title",
        max_length=40,
        min_length=3,
        strip=True,
    )
    author = forms.CharField(
        label="Author",
        max_length=40,
        min_length=3,
        strip=True,
    )
    body = forms.CharField(
        label="Body",
        max_length=300,
        min_length=3,
        widget=forms.Textarea,
        strip=True,
    )
    cover_image_url = forms.URLField(label="Cover Image Url")
