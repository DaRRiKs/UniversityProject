# UniversityProject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Импортируем RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('university/', include('university.urls')),
    path('', RedirectView.as_view(url='/university/', permanent=True)),  # Перенаправление на /university/
]
