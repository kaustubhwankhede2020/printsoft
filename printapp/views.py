from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def render_home(request):
    return render(request, "website_templates/home.html")


def render_creators_board(request):
    return render(request, "website_templates/creators_board.html")


def render_login(request):
    return render(request, "auth_templates/login.html")


def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
            else:
                return HttpResponseRedirect(reverse("employee_home"))
        else:
            return HttpResponse("Invalid Credentials")


def render_register(request):
    return render(request, "auth_templates/register.html")
