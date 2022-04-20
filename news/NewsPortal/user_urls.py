from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, SearchPost, NewsCreate, PostUpdate, PostDelete, ArticleCreate, UserUpdate


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   path('<int:pk>/update/', UserUpdate.as_view(), name='user_update'),
]