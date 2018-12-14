from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateField(auto_now_add=True)
    cover_image_url = models.URLField()

    def __str__(self):
        return f'{self.title} by {self.author}'

    @staticmethod
    def get_blogs():
        return BlogPost.objects.all()


class Comment(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    blog_id = models.ForeignKey(
        BlogPost,
        on_delete=models.PROTECT,
    )
