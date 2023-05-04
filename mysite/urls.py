# mysite/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('download_file', views.download_file, name='download_file'),
]
