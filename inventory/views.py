from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from datetime import timedelta

from .forms import MedicineForm
from .models import Medicine

@login_required
def dashboard(request):
    today = timezone.localdate()
    soon = today + timedelta(days=30)
    medicines = Medicine.objects.all()
    context = {
        "medicine_count": medicines.count(),
        "low_stock_count": medicines.filter(quantity__lte=10).count(),
        "expired_count": medicines.filter(expiry_date__lt=today).count(),
        "expiring_count": medicines.filter(expiry_date__gte=today, expiry_date__lte=soon).count(),
        "recent_medicines": medicines[:5],
    }
    return render(request, "inventory/dashboard.html", context)

@login_required
def medicine_list(request):
    query = request.GET.get("q", "").strip()
    medicines = Medicine.objects.all()
    if query:
        medicines = medicines.filter(
            Q(name__icontains=query) |
            Q(category__icontains=query) |
            Q(batch_number__icontains=query)
        )
    return render(request, "inventory/medicine_list.html", {"medicines": medicines, "query": query})

@login_required
def medicine_create(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Medicine added successfully.")
            return redirect("inventory:medicine_list")
    else:
        form = MedicineForm()
    return render(request, "inventory/medicine_form.html", {"form": form, "page_title": "Add Medicine"})

@login_required
def medicine_update(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, "Medicine updated successfully.")
            return redirect("inventory:medicine_list")
    else:
        form = MedicineForm(instance=medicine)
    return render(request, "inventory/medicine_form.html", {"form": form, "page_title": "Edit Medicine"})

@login_required
def medicine_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        medicine.delete()
        messages.success(request, "Medicine deleted successfully.")
        return redirect("inventory:medicine_list")
    return render(request, "inventory/medicine_confirm_delete.html", {"medicine": medicine})
