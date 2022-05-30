
from django.test import TestCase
# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
