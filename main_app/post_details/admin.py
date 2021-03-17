from django.contrib import admin

# Register your models here.
from .models import pending_post

admin.site.register(pending_post)