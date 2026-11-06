from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["name", "category", "batch_number", "quantity", "price", "expiry_date", "supplier"]
        widgets = {
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
        }
