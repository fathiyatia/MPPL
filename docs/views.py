from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader 
from .models import *
from .forms import DocsForms

# Create your views here.

def home(request):
    documents = Documents.objects.order_by('-date_input').all()[:9]

    context = {'documents':documents}

    return render(request, 'docs/landingpage.html', context)

def input(request):
    form = DocsForms()
    if request.method == 'POST':
        form = DocsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Surat Berhasil Ditambahkan')
            return redirect('/')

    context = {'form':form}
    return render(request, 'docs/FormInput.html', context)

def update(request, pk):
    document = Documents.objects.get(id=pk)
    id_docs = document.id
    form = DocsForms(instance=document)
    if request.method == 'POST':
        form = DocsForms(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect(detail, pk=id_docs)

    context = {'form':form, 'document':document}
    return render(request, 'docs/FormInput.html', context)

def delete(request, pk):
    document = Documents.objects.get(id=pk)
    if request.method == 'POST':
        document.delete() 
        return redirect('/')

    context = {'document':document}

    return render(request, 'docs/delete.html', context)

def detail(request, pk):
    document = Documents.objects.get(id=pk)
    context = {'document':document}
    return render(request, 'docs/detail.html', context)