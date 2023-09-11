from django.shortcuts import redirect, render
from .forms import CustomerUploadForm
from .models import Customer

def upload_customers(request):
    if request.method == "POST":
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerUploadForm()
    return render(request, 'customer/customer_upload.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer-list.html', {'customers': customers})

def customer_detail(request, user_id):
    customer = Customer.objects.get(user_id=user_id)
    return render(request, 'customer/customer_detail.html', {'customer': customer})

def edit_customer_view(request, user_id):
    customer= Customer.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = CustomerUploadForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail_view', user_id=customer.user_id)
    else:
        form = CustomerUploadForm(instance=customer)
    return render(request, 'customer/edit_customer.html', {'form': form})