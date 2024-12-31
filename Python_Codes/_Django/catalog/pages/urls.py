from django.urls import path
from . import views # import the views from the current directory

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='index'), # this is the home page
    path('about', views.about, name='about'), # this is the about page
]