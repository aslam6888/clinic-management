from django.urls import path
from .views import docter_lists, docter_details


urlpatterns = [
    path('lists', docter_lists),
    path('view/<int:id>', docter_details)
]