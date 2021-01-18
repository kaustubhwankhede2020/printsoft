"""printsoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from printapp import views, admin_views, employee_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_home, name="home"),
    path('creators_board/', views.render_creators_board, name="creators_board"),
    path('login/', views.render_login, name="login"),
    path('perform_login', views.perform_login, name="perform_login"),
    path('register/', views.render_register, name="register"),

    # render admin templates
    path('admin_home', admin_views.render_admin_home, name="admin_home"),

    # render employee templates
    path('employee_home', employee_views.render_employee_home, name="employee_home"),
]
