from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from ddos.models import DosResult


class ListViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='tester')
        self.user.set_password('password')
        self.user.save()
        self.url = reverse('service_list')

    def test_200(self):
        client = Client()
        self.assertTrue(client.login(username='tester', password='password'))
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_queryset(self):
        dos_result1 = DosResult.objects.create(name='Tester Service', identifier='123456', user=self.user)
        dos_result2 = DosResult.objects.create(name='Tester Service', identifier='12345', user=self.user)
        client = Client()
        self.assertTrue(client.login(username='tester', password='password'))
        response = client.get(self.url)
        self.assertEqual(response.context_data['object_list'].get(identifier='123456'), dos_result1)
