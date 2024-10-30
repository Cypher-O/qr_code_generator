# qr_generator/apps/generator/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class QRCodeTests(APITestCase):
    def test_generate_qr_code(self):
        data = {'data': 'http://example.com'}
        response = self.client.post(reverse('qr-code-generate'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'image/png')