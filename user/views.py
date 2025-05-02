from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = (authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']))

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error('password', 'Username yoki parol noto\'g\'ri')
    return render(request, "accounts/sign-in.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
