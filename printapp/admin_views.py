from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def render_admin_home(request):
    return render(request, "admin_templates/admin_index.html")
