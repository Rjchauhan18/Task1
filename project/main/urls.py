from django.contrib import admin
from django.urls import path,include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", home, name="Home"),
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("doctor_dashboard/", doctor_dashboard, name="doctor_dashboard"),
    path("", patient_dashboard, name="patient_dashboard"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

