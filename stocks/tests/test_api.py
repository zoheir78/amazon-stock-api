from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from stocks.models import StockPrice, Annotation
from datetime import date


class APITests(APITestCase):
    def setUp(self):
        self.stock = StockPrice.objects.create(
            date=date(2024, 1, 1),
            open=150.0,
            high=160.0,
            low=145.0,
            close=155.0,
            adj_close=155.0,
            volume=2000000,
        )

        self.annotation = Annotation.objects.create(
            date=date(2024, 1, 1), note="Test annotation", author="Tester"
        )

    # Test StockPriceListView
    def test_stockprice_list(self):
        url = reverse("stock-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # Test StockPriceDetailView
    def test_stockprice_detail(self):
        url = reverse("stock-detail", args=[self.stock.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["open"], 150.0)

    # Test AnnotationCreateView
    def test_annotation_create(self):
        url = reverse("annotation-create")
        data = {"date": "2024-01-02", "note": "Created via API", "author": "API Tester"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Annotation.objects.filter(note="Created via API").exists())

    # Test AnnotationListView
    def test_annotation_list(self):
        url = reverse("annotation-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("note", response.data["results"][0])

    # Test AnnotationDeleteView
    def test_annotation_delete(self):
        url = reverse("annotation-api-delete", args=[self.annotation.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Annotation.objects.filter(id=self.annotation.id).exists())

    # Test AnnotationUpdateView
    def test_annotation_update(self):
        url = reverse("annotation-update", args=[self.annotation.id])
        data = {"note": "Updated note"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.annotation.refresh_from_db()
        self.assertEqual(self.annotation.note, "Updated note")
