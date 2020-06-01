from django.shortcuts import render
from .models import Collection

# Create your views here.


def home(request):
    collections = Collection.objects.all()
    return render(request, 'home.html', {'collections': collections} )

