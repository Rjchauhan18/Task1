from django.contrib import admin
from django.urls import path,include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls

urlpatterns = [
    # path("", home, name="Home"),
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("doctor_dashboard/", doctor_dashboard, name="doctor_dashboard"),

    #wagtail Blog
    path("doctor_dashboard/blog/", include(wagtailadmin_urls), name="blog"),
    path("", patient_dashboard, name="patient_dashboard"),
    # path('cms/', ),
    path('documents/', include(wagtaildocs_urls)),
    # path('wagtail_url/', include(wagtail_urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)