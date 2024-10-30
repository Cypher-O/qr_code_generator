# qr_generator/apps/generator/views.py

import qrcode
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import QRCodeSerializer
from .models import QRCode
from django.core.files.base import ContentFile
import io

class QRCodeGenerateView(generics.CreateAPIView):
    serializer_class = QRCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        original_url = serializer.validated_data['original_url']

        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(original_url)
        qr.make(fit=True)

        # Create an image of the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a BytesIO object
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        # Save QR Code instance to the database
        qr_code_instance = QRCode(original_url=original_url)
        qr_code_instance.qr_code_image.save(f"{original_url.split('/')[-1]}_qrcode.png", ContentFile(img_bytes.read()))
        qr_code_instance.save()

        # Return the QR code image in response
        response = HttpResponse(content_type="image/png")
        img.save(response, "PNG")
        response['Content-Disposition'] = f'attachment; filename="{original_url.split("/")[-1]}_qrcode.png"'
        return response