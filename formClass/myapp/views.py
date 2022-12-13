from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def index(request):
    form = MyForm()
    return render(request, "myapp/index.html", {'form':form})