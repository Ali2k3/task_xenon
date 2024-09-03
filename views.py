from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("AAAAAAA")
                print(login(request, user))
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    categories = ["Apartments", "Villas", "Commercial Spaces"]
    return render(request, 'home.html', {'categories': categories})

