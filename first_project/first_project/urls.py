"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tkinter.font import names


from django.contrib import admin
from django.urls import path
from first_app import views
from first_app import views
# from first_app.views import contact_view
from first_app.views import registration_view,add_emp_form_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('show/<str:name>', views.show_data, name="show"),
    path('data_add/', views.add_data, name="add_data"),
    path('delete/<name>', views.delete_op, name="delete"),
    # path('delete/', views.delete_op, name="delete"),
    path('show/<name>', views.search_by_name, name="search"),
    path('inance/',views.inance_home, name="inance_url"),
    path('inance/about', views.inance_about, name="inance_about_url"),
    path('inance/services', views.inance_services, name="inance_services_url"),
    # path('contactform/',views.contact_view,name="contact_form_url"),
    path('registration_form/', views.registration_view, name="registration_url"),
    path('add_emp_form/', views.add_emp_form_view, name="add_emp_form_view_url"),

]
