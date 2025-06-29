from django import forms
from .models import Annotation


class DateFilterForm(forms.Form):
    start_date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"type": "date"})
    )
    end_date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"type": "date"})
    )


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ["date", "note", "author"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "note": forms.Textarea(attrs={"rows": 3}),
        }
