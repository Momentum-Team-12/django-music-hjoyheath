from django.shortcuts import render
from .models import Album
# Create your views here.


def list_albums(request):
    return render(request, 'list_albums.html', {})
