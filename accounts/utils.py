from django.core.mail import send_mail
from django.conf import settings

class MailService:
    @staticmethod
    def send_email(subject, message, recipient_list):
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )
