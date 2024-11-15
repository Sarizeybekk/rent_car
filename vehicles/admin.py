from django.contrib import admin

# Register your models here.
from .models import Marka, Model, Vehicle

admin.site.register(Marka)
admin.site.register(Model)
admin.site.register(Vehicle)