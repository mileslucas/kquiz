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
        self.user = User.objects.create_user(username='testuser', first_name='Jon', last_name='Test')
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

    def test_user_name(self):
        self.assertContains(self.index, self.user.get_full_name())

    def test_logout_link(self):
        self.assertContains(self.index, 'Logout')
        link = self.index.click('Logout')
        self.assertRedirects(link, reverse('login'))



class LoginViewTest(WebTest):
    def setUp(self):
        self.index = self.app.get(reverse('login'))
        form = self.index.form
        form['username'] = 'jont'
        form['password'] = 'test'
        self.response = form.submit('Login')

    def test_template(self):
        self.assertTemplateUsed(self.index, 'registration/login.html')

    def test_register_link(self):
        link = self.index.click('Register')
        self.assertTemplateUsed(link, 'registration/register.html')

class RegisterViewTest(WebTest):
    def setUp(self):
        self.index = self.app.get(reverse('register'))
        self.form = self.index.form
        self.form['username'] = 'jont'
        self.form['password1'] = 'test'
        self.form['password2'] = 'test'
        self.form['first_name'] = 'Jon'
        self.form['last_name'] = 'Test'
        self.response = self.form.submit()

    def test_template(self):
        self.assertTemplateUsed(self.index, 'registration/register.html')

    # def test_link(self):
    #     self.assertTemplateUsed()

class QuestionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Jon')
        self.question = Question.objects.create(text='Test Question', dispatcher=self.user, duration_factor=60, duration_value=3)

    def test_text(self):
        self.assertEqual(self.question.text, 'Test Question')

    def test_user(self):
        self.assertEqual(self.question.dispatcher, self.user)


class AnswerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Jon')
        self.question = Question.objects.create(text='Test Question', dispatcher=self.user, duration_factor=60, duration_value=3)
        self.answer = Answer.objects.create(question=self.question, researcher=self.user, text='Sample Answer')

    def test_text(self):
        self.assertEqual(self.answer.text, 'Sample Answer')

    def test_user(self):
        self.assertEqual(self.answer.researcher, self.user)

    def test_question(self):
        self.assertEqual(self.answer.question, self.question)

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jont')
        self.profile = Profile.objects.create(user=self.user)

    def test_user(self):
        self.assertEqual(self.profile.user, self.user)