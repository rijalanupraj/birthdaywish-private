# External Import
from django.urls import path

# Internal Import
from .views import homerender

urlpatterns = [
    path('', homerender, name='home-page')
]
