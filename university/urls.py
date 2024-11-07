# university/urls.py
from django.urls import path
from .views import index_view, about_view, contact_view

urlpatterns = [
    path('', index_view, name='index'),  # Это ваш маршрут для главной страницы
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]
