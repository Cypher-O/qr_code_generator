# qr_generator/apps/generator/serializers.py

from rest_framework import serializers
from .models import QRCode

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ['original_url', 'qr_code_image']
        read_only_fields = ['qr_code_image']