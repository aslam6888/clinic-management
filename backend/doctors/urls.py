from django.urls import path
from .views import doctor_lists, doctor_details, add_doctor


urlpatterns = [
    path('lists', doctor_lists),
    path('view/<int:id>', doctor_details),
    path('add', add_doctor)
]