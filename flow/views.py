import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login, logout 

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "flow/home.html", context)

def register_view(request):

    form = UserCreationForm()
    error = ""

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            error_dict = form.errors.as_data()
            formatted_errors = []

            for field, errors in error_dict.items():
                for error in errors:
                    error_string = re.sub('<.*?>', '', str(error))
                    formatted_errors.append(f"{field}: {error_string}")

            error = '\n'.join(formatted_errors)

    context = {"form": form, "error": error}
    return render(request, "flow/register.html", context)