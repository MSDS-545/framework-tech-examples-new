"""A minimal test showing Django's built-in test client."""
from django.test import TestCase
class HomePageTest(TestCase):
    def test_home_page_returns_200(self):
        # self.client simulates a browser request without starting a real server.
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
