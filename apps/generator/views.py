# qr_generator/apps/generator/views.py

import qrcode
from django.shortcuts import render
from django.core.files.base import ContentFile
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework import status
from .serializers import QRCodeSerializer
from .models import QRCode
from .utils.api_response import APIResponse
import io

class QRCodeGenerateView(generics.CreateAPIView):
    serializer_class = QRCodeSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        # Render the HTML template for GET requests
        return render(request, 'generator/qr_code_generator.html')

    def post(self, request, *args, **kwargs):
        # Handle API requests
        if request.content_type == 'application/json':
            original_url = request.data.get('original_url')
        else:
            original_url = request.POST.get('original_url')

        if not original_url:
            return APIResponse.validation_error(
                message="original_url is required",
                errors={"original_url": ["This field is required."]}
            )

        try:
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
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes.seek(0)

            # Save QR Code instance to the database
            qr_code_instance = QRCode(original_url=original_url)
            qr_code_instance.qr_code_image.save(
                f"qrcode_{original_url[:30]}.png",
                ContentFile(img_bytes.read()),
                save=True
            )

            # Return appropriate response based on request type
            if request.content_type != 'application/json':
                return render(request, 'generator/qr_code_generator.html', {
                    'qr_code': qr_code_instance.qr_code_image.url,
                    'success': True
                })
            
            serializer = self.get_serializer(qr_code_instance)
            return APIResponse.success(
                data=serializer.data,
                message="QR Code generated successfully",
                status_code=status.HTTP_201_CREATED
            )

        except Exception as e:
            return APIResponse.error(
                message="Failed to generate QR code",
                data={"error": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

def home(request):
    return render(request, 'generator/qr_code_generator.html')
