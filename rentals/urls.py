from django.urls import path
from . import views
urlpatterns = [
        path('create/', views.create_rental, name='create_rental'),
    path('list/', views.rental_list, name='rental_list'),
]