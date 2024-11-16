from django.core.mail import send_mail
from django.conf import settings
from django.template import Context, Template
from .models import MailTemplate
from .enums import MailTemplates

class MailService:
    @staticmethod
    def send_email(template_enum: MailTemplates, context, recipient_list):
        try:
            # Şablonu veritabanından getir
            template = MailTemplate.objects.get(name=template_enum.value)  # Enum'dan değer alınıyor
            
            # Şablon içeriğini render et
            template_body = Template(template.body).render(Context(context))
            
            # Mail gönder
            send_mail(
                subject=template.subject,
                message="",  # Plain text kısmı boş bırakıldı
                html_message=template_body,  # HTML formatında e-posta
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipient_list,
                fail_silently=False,
            )
        except MailTemplate.DoesNotExist:
            raise ValueError(f"No mail template found with name '{template_enum.value}'")
