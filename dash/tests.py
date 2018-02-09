import socket
from django.test import TestCase, LiveServerTestCase, override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

# Create your tests here.


### Selenium Tests ###
@override_settings(ALLOWED_HOSTS=['*'])  # Disable ALLOW_HOSTS
class BaseSeleniumTest(StaticLiveServerTestCase):
    """
    Provides base test class which connects to the Docker
    container running Selenium.
    """
    host = '0.0.0.0'

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.host = socket.gethostbyname(socket.gethostname())
        # Instantiate the remote WebDriver
        self.selenium = webdriver.Remote(
            command_executor=os.getenv('SELENIUM_HOST'),
            desired_capabilities=DesiredCapabilities.CHROME,
        )
        self.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(self):
        self.selenium.quit()
        super().tearDownClass()

class ConnectionTest(BaseSeleniumTest):
    def test_register(self):
        browser = self.selenium
        browser.get(self.live_server_url)
        self.assertIn('Hello', browser.title)
