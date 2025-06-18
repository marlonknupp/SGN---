from django.shortcuts import render
from .models import Notebook

def lista_notebook(request):
    notebook = Notebook.objects.all()
    return render (request, 'notebook/lista.html', {'notebooks': notebook})
