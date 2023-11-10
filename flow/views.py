from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "flow/home.html", context)

def register_view(request):
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "flow/register.html", context)