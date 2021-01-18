from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def render_employee_home(request):
    return render(request, "employee_templates/employee_index.html")
