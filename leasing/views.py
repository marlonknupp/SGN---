from django.shortcuts import render, redirect
from .models import Leasing
from .forms import LeasingForm
from django.contrib import messages


def lista_leasing(request):
    leasings = Leasing.objects.all()
    return render(request, 'leasing/lista.html', {'leasings': leasings})

def location_user(request):
    if request.method == 'POST':
        form = LeasingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_leasing')
        
    else:
        form = LeasingForm()
        return render(request, 'leasing/location_user.html', {'form': form})
