# Generated by Django 5.1.3 on 2024-11-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images/'),
        ),
    ]
