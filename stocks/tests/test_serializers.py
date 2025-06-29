from rest_framework.test import APITestCase
from stocks.serializers import StockPriceSerializer, AnnotationSerializer
from stocks.models import StockPrice, Annotation
from datetime import date


class StockPriceSerializerTest(APITestCase):
    def setUp(self):
        self.stock_data = {
            "date": "2024-01-01",
            "open": 150.0,
            "high": 160.0,
            "low": 145.0,
            "close": 155.0,
            "adj_close": 155.0,
            "volume": 2000000,
        }

    def test_valid_stock_serializer(self):
        serializer = StockPriceSerializer(data=self.stock_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["close"], 155.0)

    def test_invalid_stock_serializer_missing_field(self):
        data = self.stock_data.copy()
        del data["date"]
        serializer = StockPriceSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("date", serializer.errors)


class AnnotationSerializerTest(APITestCase):
    def setUp(self):
        self.annotation_data = {
            "date": "2024-01-01",
            "note": "Test note",
            "author": "TestUser",
        }

    def test_valid_annotation_serializer(self):
        serializer = AnnotationSerializer(data=self.annotation_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["author"], "TestUser")

    def test_invalid_annotation_serializer_missing_note(self):
        data = self.annotation_data.copy()
        del data["note"]
        serializer = AnnotationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("note", serializer.errors)
