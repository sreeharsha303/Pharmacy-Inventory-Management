from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "batch_number", "quantity", "price", "expiry_date")
    search_fields = ("name", "category", "batch_number")
    list_filter = ("category", "expiry_date")
