from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MailTemplate
from tinymce.widgets import TinyMCE
from django.db import models



class MailTemplateAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(MailTemplate, MailTemplateAdmin)