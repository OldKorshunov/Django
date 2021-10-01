from django.urls import path, re_path

from .views import (index, main_article, archive_article, users, hexadecimal, random_slug, random_page,article_number, article_text, article_user_number, phone_number, first)


urlpatterns = [
    path('', index, name='index'),
    path('first', first, name='first'),
    path('articles', main_article, name='main_article'),
    path('articles/archive/', archive_article, name='archive_article'),
    path('users/', users, name='users'),
    path('random_page/', random_page, name='random_page'),
    path('random_slug/', random_slug, name='random_slug'),
    path('article/<int:article_number>/', article_number, name='article_number'),
    path('article/<int:article_number>/<slug:slug_text>', article_text, name='article_text'),
    path('users/<int:user_number>/', article_user_number, name='article_user_number'),
    re_path(r'^articles/(0(50|63|95)([0-9]{7}))/', phone_number, name='phone_number'),
    re_path(r'^articles/(([a-f]|[0-9]){4}-([a-f]|[0-9]){6})/', hexadecimal, name='hexadecimal')
]
