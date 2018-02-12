from django.test import TestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django_webtest import WebTest
from django.utils import timezone

from dash.views import *
from dash.models import *
# Create your tests here.


class IndevViewTest(WebTest):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.index = self.app.get(reverse('index'), user=self.user)

    def test_login_if_not_authorized(self):
        # Uses one-off unauthroized client
        response = Client().get(reverse('index'))
        self.assertRedirects(response, reverse('login') + '?next=/')

    def test_template(self):
        self.assertTemplateUsed(self.index, 'dash/index.html')

    def test_text(self):
        self.assertContains(self.index, 'Choose View')

    def test_links_dispatcher(self):
        link = self.index.click('Dispatcher')
        self.assertTemplateUsed(link, 'dash/dispatcher/dispatcher.html')

    def test_links_researcher(self):
        link = self.index.click('Researcher')
        self.assertTemplateUsed(link, 'dash/researcher/researcher.html')

class LoginViewTest(WebTest):
    def setUp(self):
        self.index = self.app.get(reverse('login'))
        form = self.index.form
        form['username'] = 'root'
        form['password'] = 'merl1nd0g'
        self.response = form.submit('Login')

    def test_template(self):
        self.assertTemplateUsed(self.index, 'registration/login.html')



class QuestionModelTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text='Test Question')

    def test_text(self):
        self.assertEqual(self.question.text, 'Test Question')


class AnswerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Jon', password='Test')
        self.question = Question.objects.create(text='Test Question')
        self.answer = Answer.objects.create(question=self.question, researcher=self.user, text='Sample Answer')

    def test_text(self):
        self.assertEqual(self.answer.text, 'Sample Answer')

    def test_user(self):
        self.assertEqual(self.answer.researcher, self.user)

    def test_question(self):
        self.assertEqual(self.answer.question, self.question)

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Jon', password='Test')
        self.profile = Profile.objects.create(user=self.user)

    def test_user(self):
        self.assertEqual(self.profile.user, self.user)