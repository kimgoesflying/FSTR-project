from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from mountain_pass.models import MountainPass, Tourist, MountainPassImage

from apis.serializers import MountainPassSerializer
import base64
from .binary_img import BINARY_IMAGE

MOUNTAINPASS_LIST_URL = reverse('list_mountain_pass')


class MountainPassTestApi(TestCase):
    """Test the publicly available MountainPass API"""

    def setUp(self):
        self.client = APIClient()

        self.title = "Перевал Горных Духов"
        self.status = 'new'
        self.latitude = 51.93139
        self.longitude = 101.70625
        self.height = 2880

        self.tourist_email = "zagulyai@mail.mail"
        self.tourist_first_name = "Елена"
        self.tourist_middle_name = "Владимировна"
        self.tourist_last_name = "Загуляй"
        self.tourist_phone = "+79031234567"

        self.binary_image = base64.b64decode(str(BINARY_IMAGE))
        self.image_title = "Перевал Горных Духов"

    def test_retrieve_MountainPass(self):
        """Test for retrieving all MountainPass"""

        self.tourist = Tourist.objects.create(
            email=self.tourist_email,
            first_name=self.tourist_first_name,
            middle_name=self.tourist_middle_name,
            last_name=self.tourist_last_name,
            phone=self.tourist_phone)

        self.mountainpass = MountainPass.objects.create(
            user=self.tourist,
            title=self.title,
            status=self.status,
            latitude=self.latitude,
            longitude=self.longitude,
            height=self.height,
        )

        self.mountainpass_images = MountainPassImage.objects.create(
            mountainpass=self.mountainpass,
            binary_image=self.binary_image,
            title=self.image_title,
        )

        res = self.client.get(MOUNTAINPASS_LIST_URL)

        mountain_pass_list = MountainPass.objects.all()
        serializer = MountainPassSerializer(mountain_pass_list, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_MountainPass(self):
        """Test for creating MountainPass"""

        tourist = {
            'email': self.tourist_email,
            'first_name': self.tourist_first_name,
            'middle_name': self.tourist_middle_name,
            'last_name': self.tourist_last_name,
            'phone': self.tourist_phone
        }

        image_data = [{
            'image_base64': base64.b64encode(self.binary_image).decode('utf8'),
            'title': self.image_title,
        }]

        payload = {
            'title': self.title,
            "status": self.status,
            'user': tourist,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'height': self.height,
            'images': image_data
        }

        self.client.post(MOUNTAINPASS_LIST_URL, payload, format="json")

        exists = MountainPass.objects.filter(
            title=payload['title'],
        ).exists()
        self.assertTrue(exists)
