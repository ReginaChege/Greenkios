from django.shortcuts import redirect, render
from .forms import VendorForm

def vendor_registration(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list_view')  
    else:
        form = VendorForm()
    
    return render(request, 'vendor/vendor-onboard.html', {'form': form})