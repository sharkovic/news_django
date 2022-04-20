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
   path('', PostList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search_post/', SearchPost.as_view()),
   path('search_post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('news/create/', NewsCreate.as_view(), name='post_create'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
   path('article/create/', ArticleCreate.as_view(), name='post_create'),
   path('article/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('article/<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
   path('user/<int:pk>/update/', UserUpdate.as_view(), name='user_update'),
]