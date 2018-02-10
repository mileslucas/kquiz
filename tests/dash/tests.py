from django.test import TestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User


from dash.views import *
# Create your tests here.


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser')
        self.client.force_login(self.user)
        self.response = self.client.get(reverse('index'))

    def test_login_if_not_authorized(self):
        # Uses one-off unauthroized client
        response = Client().get(reverse('index'))
        self.assertRedirects(response, reverse('login') + '?next=/')

    def test_template(self):
        self.assertTemplateUsed(self.response, 'dash/index.html')

    def test_text(self):
        self.assertContains(self.response, 'Choose View')
