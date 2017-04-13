from django.shortcuts import render, HttpResponse
from accounts.models import User


def home_page(request):
    users = User.objects.all()
    return render(request, "home_page.html", {"users": users})


