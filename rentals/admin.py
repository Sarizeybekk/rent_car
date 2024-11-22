from django.contrib import admin
from .models import Rental

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'customer', 'rental_date', 'return_date', 'rental_fee', 'damage_status')
    list_filter = ('rental_date', 'return_date', 'vehicle')
