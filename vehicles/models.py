from django.db import models

# Create your models here.

class Marka(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand.name} {self.name}"

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=15, unique=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=20)
    transmission_type = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    mileage = models.IntegerField()
    insurance_expiry = models.DateField()

    def __str__(self):
        return f"{self.license_plate} ({self.model})"