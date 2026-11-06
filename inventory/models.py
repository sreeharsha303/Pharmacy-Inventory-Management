from django.db import models
from django.utils import timezone
from datetime import timedelta

class Medicine(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    batch_number = models.CharField(max_length=50, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()
    supplier = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.batch_number})"

    @property
    def stock_status(self):
        if self.quantity <= 10:
            return "Low stock"
        return "In stock"

    @property
    def expiry_status(self):
        today = timezone.localdate()
        if self.expiry_date < today:
            return "Expired"
        if self.expiry_date <= today + timedelta(days=30):
            return "Expiring soon"
        return "Good"
