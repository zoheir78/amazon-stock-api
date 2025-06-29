from django.test import TestCase
from stocks.models import StockPrice, Annotation
from datetime import date


class StockPriceModelTest(TestCase):
    def test_stock_price_str(self):
        stock = StockPrice.objects.create(
            date=date(2024, 1, 1),
            open=150.0,
            high=160.0,
            low=145.0,
            close=155.0,
            adj_close=155.0,
            volume=1000000,
        )
        self.assertEqual(str(stock), "2024-01-01 - Close: 155.0")


class AnnotationModelTest(TestCase):
    def test_annotation_str(self):
        annotation = Annotation.objects.create(
            date=date(2024, 1, 1),
            note="This is a test annotation for stock movement.",
            author="TestUser",
        )
        expected_str = "2024-01-01 - TestUser: This is a test annotation for "
        self.assertEqual(str(annotation), expected_str)

    def test_annotation_default_author(self):
        annotation = Annotation.objects.create(
            date=date(2024, 1, 2), note="Anonymous author test"
        )
        self.assertEqual(annotation.author, "Anonymous")
