from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum


class Author(models.Model):
    name = models.CharField(max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    def update_rating(self):
        rating_post = self.post_set.aggregate(postrating=Sum('rating_post'))
        rp = rating_post.get('postrating')
        rating_comment = self.user.comment_set.aggregate(comrating=Sum('rating_comment'))
        rc = rating_comment.get('comrating')
        self.rating = rp * 3 + rc
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.name_category}'

article = 'article'
news = 'news'
ARTICLEORNEWS = [
    (article, 'Статья'),
    (news, 'Новость')

]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    area_post = models.CharField(max_length=7,
                                 choices=ARTICLEORNEWS)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory', related_name='category')
    title_post = models.CharField(max_length=50)
    text_post = models.CharField(max_length=9999)
    rating_post = models.IntegerField(default=0)



    def preview(self):
        return f"{self.text_post[:125]}..."

    def like(self):
        if self.rating_post >= 0:
            self.rating_post += 1
        self.save()

    def dislike(self):
        if self.rating_post > 0:
            self.rating_post -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.CharField(max_length=255)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        if self.rating_comment >= 0:
            self.rating_comment += 1
        self.save()

    def dislike(self):
        if self.rating_comment > 0:
            self.rating_comment -= 1
        self.save()
