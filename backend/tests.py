from django.test import TestCase
from .models import FGFPost
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status # Definitely use this
from rest_framework.test import APIClient, APITestCase

# python manage.py test

class FGFPostTestCase(APITestCase):
  def setUp(self):
    self.admin_user = User.objects.create_superuser(username='NewUser', password='testing!88')
    self.data_good = {"title":"[Steam] (Game) Halo 3", "author":"/u/Garry", "reddit_id":"1234567"}
    self.data_bad = {"title":"Missing Stuff"}

  def test_fgfpost_viewing_unauthenticated(self):
    response = self.client.get(reverse('fgfpost-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_fgfpost_creation_unauthenticated(self):
    response = self.client.post(reverse("fgfpost-list"), self.data_good)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_fgfpost_creation_missing_fields(self):
    self.user = User.objects.get(username='NewUser')
    self.client.force_login(self.user)

    response = self.client.post(reverse("fgfpost-list"), self.data_bad, format='json')

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_fgfpost_creation_authenticated(self):
    self.user = User.objects.get(username='NewUser')
    self.client.force_login(self.user)

    response = self.client.post(reverse("fgfpost-list"), self.data_good, format='json')

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_fgfpost_update_unauthenticated(self):
    response = self.client.put(reverse("fgfpost-detail", kwargs={"pk":1}), self.data_good, format='json')

    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_fgfpost_update_authenticated(self):
    self.user = User.objects.get(username='NewUser')
    self.client.force_login(self.user)
    self.client.post(reverse("fgfpost-list"), self.data_good, format='json')

    response = self.client.put(reverse("fgfpost-detail", kwargs={"pk":1}), self.data_good, format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_fgfpost_update_authenticated_bad_data(self):
    self.user = User.objects.get(username='NewUser')
    self.client.force_login(self.user)
    self.client.post(reverse("fgfpost-list"), self.data_good, format='json')

    response = self.client.put(reverse("fgfpost-detail", kwargs={"pk":1}), self.data_bad, format='json')

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_fgfpost_delete_unauthenticated(self):
    #Creating dummy post while logged in (I should've just created an item in setup ouch)
    self.user = User.objects.get(username='NewUser')
    self.client.force_login(self.user)
    self.client.post(reverse("fgfpost-list"), self.data_good, format='json')
    #Logging out when done
    self.client.logout()

    response = self.client.delete(reverse("fgfpost-detail", kwargs={"pk":1}))

    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_fgfpost_delete_authenticated(self):
    self.user = User.objects.get(username='NewUser')
    self.client.force_login(self.user)
    self.client.post(reverse("fgfpost-list"), self.data_good, format='json')

    response = self.client.delete(reverse("fgfpost-detail", kwargs={"pk":1}))

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)





# from django.test import TestCase
# from api.models import Order, User
# from django.urls import reverse
# from rest_framework import status

# class UserOrderTestCase(TestCase):
#     def setUp(self):
#         user1 = User.objects.create_user(username='user1', password='test')
#         user2 = User.objects.create_user(username='user2', password='test')
#         Order.objects.create(user=user1)
#         Order.objects.create(user=user1)
#         Order.objects.create(user=user2)
#         Order.objects.create(user=user2)

#     def test_user_order_endpoint_retrieves_only_authenticated_user_orders(self):
#         user = User.objects.get(username='user2')
#         self.client.force_login(user)
#         response = self.client.get(reverse('user-orders'))

#         assert response.status_code == status.HTTP_200_OK
#         orders = response.json()
#         self.assertTrue(all(order['user'] == user.id for order in orders))

#     def test_user_order_list_unauthenticated(self):
#         response = self.client.get(reverse('user-orders'))
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
