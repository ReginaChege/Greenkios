from django.shortcuts import render
from .forms import PaymentUploadForm

def create_payment(request):
    if request.method == 'POST':
        form = PaymentUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PaymentUploadForm()
    
    return render(request, 'payment/create_payment.html', {'form': form})

