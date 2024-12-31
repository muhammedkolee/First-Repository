from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# http://127.0.0.1:8000/


# to run this view, add this to the urls.py file in the app folder
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')