from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import  resolve
from lists.views import home_page
from django.http import HttpRequest
# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
    #     found = resolve('/')
    #     self.assertEqual(found.func,home_page)
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf-8')
    #     # self.assertTrue(html.startswith('<html>'))
    #     # self.assertIn('<title>To-Do lists</title>',html)
    #     # self.assertTrue(html.endswith('</html>'))
    #     expected_html = render_to_string('home.html')
    #     self.assertEqual(html,expected_html)
