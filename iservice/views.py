from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required(login_url="login")
def calendar_view(request):
    return render(request, 'calendar.html')

@login_required(login_url="login")
def employees_view(request):
    return render(request, 'employees.html')
