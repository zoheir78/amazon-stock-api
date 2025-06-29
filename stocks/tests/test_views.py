from django.test import TestCase, Client
from django.urls import reverse
from stocks.models import StockPrice, Annotation
from datetime import date
from django.utils.http import urlencode


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Create test stock
        self.stock = StockPrice.objects.create(
            date=date(2024, 1, 1),
            open=100,
            high=110,
            low=90,
            close=105,
            adj_close=105,
            volume=15_000_000,
        )

        # Create test annotation
        self.annotation = Annotation.objects.create(
            date=date(2024, 1, 1), note="Initial annotation", author="Tester"
        )

    def test_landing_page_get(self):
        response = self.client.get(reverse("landing"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stocks/landing.html")

    def test_landing_page_filtering_by_date(self):
        response = self.client.get(
            reverse("landing"), {"start_date": "2024-01-01", "end_date": "2024-01-02"}
        )
        self.assertContains(response, "Amazon Stock Data")  # Title
        self.assertEqual(len(response.context["page_obj"]), 1)

    def test_landing_page_filtering_high_volume(self):
        response = self.client.get(reverse("landing"), {"high_volume": "1"})
        self.assertEqual(len(response.context["page_obj"]), 1)

    def test_annotation_create_post(self):
        response = self.client.post(
            reverse("landing"),
            {"date": "2024-01-02", "note": "New note from test", "author": "TestBot"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Annotation.objects.filter(note="New note from test").exists())

    def test_annotation_update_post(self):
        response = self.client.post(
            reverse("landing"),
            {
                "update_id": self.annotation.id,
                "date": "2024-01-01",
                "note": "Updated note",
                "author": "Tester",
            },
        )
        self.assertRedirects(response, reverse("landing"))
        self.annotation.refresh_from_db()
        self.assertEqual(self.annotation.note, "Updated note")

    def test_annotation_delete_view(self):
        delete_url = reverse("annotation-delete", args=[self.annotation.id])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Annotation.objects.filter(id=self.annotation.id).exists())

    def test_annotation_delete_404(self):
        delete_url = reverse("annotation-delete", args=[9999])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 404)
