from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UserViewSetTestCase(APITestCase):

    fixtures = ['test_user']

    def test_list(self):
        # https://www.django-rest-framework.org/api-guide/routers/#simplerouter
        url = reverse('blog:users-list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        users = response.data['results']
        self.assertEqual(len(users), 2)

class EntryViewSetTestCase(APITestCase):
    fixtures = ['test_user', 'test_entry']

    def test_list(self):
        url = reverse('blog:entries-list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entries = response.data['results']
        self.assertEqual(len(entries), 1)
