from django.urls import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'vehicles'  # Bu satır namespace'i tanımlar
urlpatterns = [
    path('list/', views.vehicle_list, name='vehicle_list'),  # Burada "list/" olarak değiştirdik
    path('<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('cart/', views.cart, name='cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

