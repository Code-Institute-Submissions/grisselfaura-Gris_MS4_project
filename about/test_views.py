from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Portfolio

class TestAboutViews(TestCase):

    def test_get_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/about.html")

    def test_connect_view_url_exists_at_desired_location(self):
        response = self.client.get('/about/connect/')
        self.assertEqual(response.status_code, 200)

    def test_get_connect_page(self):
        response = self.client.get("/about/connect/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/connect.html")

    def test_get_portfolio_page(self):
        response = self.client.get("/about/portfolio/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/portfolio.html")

    # def test_get_portfolio_slider_page(self):
    #     response = self.client.get("/about/1/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "about/portfolio_slide_vertical.html")

