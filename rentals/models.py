from django.db import models

# Create your models here.
from vehicles.models import Vehicle
from accounts.models import CustomUser

class Rental(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField()
    rental_fee = models.DecimalField(max_digits=10, decimal_places=2)
    damage_status = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.username} - {self.vehicle.license_plate}"