from django.shortcuts import render, redirect, get_object_or_404
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

def ver_leasing(request, pk):
    leasing = get_object_or_404(Leasing, pk=pk)
    return render(request, 'leasing/ver.html', {'leasing': leasing})

def editar_leasing(request, pk):
    leasing = get_object_or_404(Leasing, pk=pk)
    if request.method == 'POST':
        form = LeasingForm(request.POST, instance=leasing)
        if form.is_valid():
            form.save()
            return redirect('lista_leasing')
    else:
        form = LeasingForm(instance=leasing)
    return render(request, 'leasing/form.html', {'form': form})

def deletar_leasing(request, pk):
    leasing = get_object_or_404(Leasing, pk=pk)
    if request.method == 'POST':
        Leasing.delete()
        return redirect('lista_leasing')
    return render(request, 'leasing/confirmar_delete.html', {'leasing': leasing})
