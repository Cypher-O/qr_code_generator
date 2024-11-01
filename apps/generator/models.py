# qr_generator/apps/generator/models.py

from django.db import models

class QRCode(models.Model):
    original_url = models.URLField(max_length=2000)
    qr_code_image = models.ImageField(upload_to='qr_codes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
    