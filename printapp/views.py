from django.shortcuts import render


# Create your views here.
def render_home(request):
    return render(request, "website_templates/home.html")


def render_creators_board(request):
    return render(request, "website_templates/creators_board.html")


def render_login(request):
    return render(request, "auth_templates/login.html")


def render_register(request):
    return render(request, "auth_templates/register.html")
