from django.shortcuts import render,redirect
from .forms import DeliveryForm
from .models import Deliver
# Create your views here.

def place_delivery(request):
    form=DeliveryForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form=DeliveryForm()
        
    return render(request, 'delivery/place_delivery.html', {'form':form})

def delivery_list(request):
    deliverys = Deliver.objects.all()
    return render(request, 'delivery/delivery_list.html', {'deliverys': deliverys})

def edit_delivery_view(request, id):
    delivery = Deliver.objects.get(id=id)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect('product_detail_view', id=delivery.id)
    else:
        form = DeliveryForm(instance=delivery)
    return render(request, 'inventory/edit_delivery.html', {'form': form})