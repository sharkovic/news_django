from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def update_rating(self):

        t = sum(Post.rating_post)

class Category(models.Model):
    name_category = models.CharField(max_length=20, unique=True)


class Post(models.Model):
    article = 'article'
    news = 'news'
    ARTICLEORNEWS = [
        (article, 'Статья'),
        (news, 'Новость')

    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    area_post = models.CharField(max_length=7,
                                 choices=ARTICLEORNEWS)
    date_of_creation = models.DateTimeField(default=datetime.now())
    category = models.ManyToManyField(Category, through='PostCategory')
    title_post = models.CharField(max_length=50)
    text_post = models.CharField()
    rating_post = models.IntegerField(default=0)

    def preview(self):
        return f"{self.text_post[:124]}..."

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.CharField()
    date_of_creation = models.DateTimeField(default=datetime.now())
    rating_comment = models.IntegerField(default=0)

    def like(self):
        if self.rating_comment >= 0:
            self.rating_comment += 1
        self.save()

    def dislike(self):
        if self.rating_comment > 0:
            self.rating_comment -= 1
        self.save()

