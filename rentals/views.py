from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Rental
from .forms import RentalForm
from vehicles.models import Vehicle  # Araç modeli
@login_required
def create_rental(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        vehicle_id = request.POST.get('vehicle')
        rental_date = request.POST.get('rental_date')
        return_date = request.POST.get('return_date')
        additional_info = request.POST.get('information')

        # Araç kontrolü
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
        except Vehicle.DoesNotExist:
            messages.error(request, "Seçilen araç mevcut değil.")
            return redirect('create_rental')

        # Tarih uygunluk kontrolü
        if Rental.objects.filter(
            vehicle=vehicle,
            rental_date__lte=return_date,
            return_date__gte=rental_date
        ).exists():
            messages.error(request, "Bu araç seçili tarihlerde uygun değil.")
        else:
            # Yeni rezervasyon oluştur
            Rental.objects.create(
                vehicle=vehicle,
                customer=request.user,
                rental_date=rental_date,
                return_date=return_date,
                rental_fee=200.00,  # Sabit bir ücret, dinamik olarak hesaplanabilir
                damage_status=additional_info or "Hasar durumu belirtilmedi"
            )
            messages.success(request, "Araç başarıyla rezerve edildi.")
            return redirect('rental_list')  # Kiralama listesi sayfasına yönlendirme

    # GET isteği: Formu ve araç listesini göster
    vehicles = Vehicle.objects.all()
    return render(request, 'rentals/create_rental.html', {'vehicles': vehicles})
@login_required
def rental_list(request):
    rentals = Rental.objects.filter(customer=request.user)
    return render(request, 'rentals/rental_list.html', {'rentals': rentals})
