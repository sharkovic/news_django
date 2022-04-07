from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum


class Author(models.Model):
    name = models.CharField(max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def update_rating(self):
        rating_post = Post.objects.filter(author=self).aggregate(postrating=Sum('rating_post'))
        self.rating_post = rating_post['postrating']
        rating_comment = Comment.objects.filter(user=self.user.id).aggregate(comrating=Sum('rating_comment'))
        self.rating_comment = rating_comment['comrating']

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
    text_post = models.CharField(max_length=9999)
    rating_post = models.IntegerField(default=0)

    def preview(self):
        return f"{self.text_post[:124]}..."

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.CharField(max_length=255)
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

