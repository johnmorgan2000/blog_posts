from django.shortcuts import render
from django.views import View
from . import models

# Create your views here.


class HomePage(View):
    def get(self, request):
        return render(request, "home.html",
                      {'blog_posts': models.BlogPost.get_blogs()})
