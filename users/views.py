from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import login
# Create your views here.

def registerView(request): 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'pages/home.html')
        else: 
            return render(request, 'registration/register.html', {"form": form})
    
    else: 
        return render(request, "registration/register.html", {"form": CustomUserCreationForm()})
