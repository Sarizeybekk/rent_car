from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from tinymce.models import HTMLField



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
    

class MailTemplate(models.Model):
    name = models.CharField(max_length=255)  # Template adı (ör. Hoş Geldiniz)
    subject = models.CharField(max_length=255)  # E-postanın konu başlığı
    body = HTMLField()  # TinyMCE tarafından düzenlenebilir alan

    def __str__(self):
        return self.name