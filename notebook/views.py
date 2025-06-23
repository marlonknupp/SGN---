from django.shortcuts import render, get_object_or_404, redirect
from .models import Notebook

def lista_notebook(request):
    notebook = Notebook.objects.all()
    return render (request, 'notebook/lista.html', {'notebooks': notebook})

def ver_notebook(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    return render(request, 'notebook/ver.html', {'notebook': notebook})

