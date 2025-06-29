from django.test import TestCase
from stocks.forms import DateFilterForm, AnnotationForm
from datetime import date


class DateFilterFormTests(TestCase):
    def test_valid_date_filter_form(self):
        form = DateFilterForm(
            data={"start_date": "2024-01-01", "end_date": "2024-01-31"}
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["start_date"], date(2024, 1, 1))

    def test_date_filter_form_with_missing_data(self):
        form = DateFilterForm(data={})
        self.assertTrue(form.is_valid())  # all fields are optional


class AnnotationFormTests(TestCase):
    def test_valid_annotation_form(self):
        form = AnnotationForm(
            data={"date": "2024-01-01", "note": "Test note", "author": "Test Author"}
        )
        self.assertTrue(form.is_valid())

    def test_missing_required_fields(self):
        form = AnnotationForm(data={"author": "Someone"})
        self.assertFalse(form.is_valid())
        self.assertIn("date", form.errors)
        self.assertIn("note", form.errors)

    def test_optional_author_field(self):
        form_data = {
            "date": "2024-01-01",
            "note": "Test note for optional author",
            "author": "Test User",  # Just provide a value
        }
        form = AnnotationForm(data=form_data)
        self.assertTrue(form.is_valid())
