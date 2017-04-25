from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from accounts.forms import LoginForm, RegistrationForm
from accounts.models import User


def home_page(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create(email=data.get("email"),
                                password=data.get("password"),
                                photo=data.get("photo"),
                                birth_date=data.get("birth_date"))
    return render(request, "home_page.html", {"form": form})


@login_required(login_url="/login/")
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def sign_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("home"))
    else:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(email=data.get("email"), password=data.get("password"))
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    print("sorry")
        return render(request, "login.html", {"form": form})
