from django.contrib.auth.models import AbstractUser
from django.db import models
from wagtail.models import Page

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel 

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Patient')
    photo = models.ImageField(default='images/default.jpg',upload_to='images/', blank=True, null=True)  


class BlogPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    template = "doctor/blog_page.html"
