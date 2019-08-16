from django.contrib import admin
from .models import user
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["username", "phone"]}),
        ("Content", {"fields": ["email"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }



admin.site.register(user)