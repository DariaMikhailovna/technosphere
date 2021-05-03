from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render


@login_required
def home(request):
    print(request.user)
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')