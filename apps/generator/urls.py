# qr_generator/apps/generator/urls.py

from django.urls import path
from .views import QRCodeGenerateView

urlpatterns = [
    path('generate', QRCodeGenerateView.as_view(), name='generate_qr_code'),
]