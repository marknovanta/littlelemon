from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(name='Item 1', price=10.0)
        self.menu2 = Menu.objects.create(name='Item 2', price=15.0)
        self.menu3 = Menu.objects.create(name='Item 3', price=20.0)

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)