from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.enums import MailTemplates
from .forms import RegisterForm, LoginForm
from .utils import MailService  # SMTP işlemleri için yardımcı sınıf

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Mail için context
            context = {
                'user': user,  
            }
            # Mail gönder
            MailService.send_email(
                template_enum=MailTemplates.WELCOME_EMAIL,  # Enum kullanılıyor
                context=context,
                recipient_list=[user.email]
            )
            
            messages.success(request, "Your account has been created!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Giriş Görünümü
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Anasayfaya yönlendir
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# Çıkış Görünümü
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
