from django.shortcuts import render
from .models import Feature

# Create your views here.
def index(request):
    writing = Feature.objects.all()
    return render(request, 'index.html', {'writing': writing})

def post(request, pk):
    writing = Feature.objects.get(id=pk)
    return render(request, 'post.html',  {'writing': writing})
