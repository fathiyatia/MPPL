from django.shortcuts import render, redirect
from django.template import loader 
from .models import *
from .forms import DocsForms
from .filters import DocsFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage 

# Create your views here.

#  login page
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username atau Password tidak sesuai')

    context = {}
    return render(request, 'docs/login.html', context)

# log out
def logoutUser(request):
	logout(request)
	return redirect('login')

# rendering landing page
@login_required(login_url='login')
def home(request):
    documents = Documents.objects.order_by('-date_input').all()[:9]

    # filtering
    docs_filter = DocsFilter(request.GET, queryset=documents)
    documents = docs_filter.qs

    context = {'documents':documents, 'docs_filter':docs_filter}

    return render(request, 'docs/landingpage.html', context)

# rendering search page
@login_required(login_url='login')
def search(request):
    documents = Documents.objects.all()

    # filtering
    docs_filter = DocsFilter(request.GET, queryset=documents)
    documents = docs_filter.qs

    context = {'documents':documents, 'docs_filter':docs_filter}

    return render(request, 'docs/searchPage.html', context)

#  create document
@login_required(login_url='login')
def input(request):
    form = DocsForms()
    if request.method == 'POST':
        form = DocsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Surat Berhasil Ditambahkan')
            return redirect('/')

    context = {'form':form}
    return render(request, 'docs/FormInput.html', context)

#  update/edit document 
@login_required(login_url='login')
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

# deleting document
@login_required(login_url='login')
def delete(request, pk):
    document = Documents.objects.get(id=pk)
    if request.method == 'POST':
        document.delete() 
        return redirect('/')

    context = {'document':document}

    return render(request, 'docs/delete.html', context)

#  showing user profile  
@login_required(login_url='login')   
def profile(request):
    # user = User.objects.get(id=pk)
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name
    context = {'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name}
    return render(request, 'docs/profile.html', context)

#  showing document details
@login_required(login_url='login')
def detail(request, pk):
    document = Documents.objects.get(id=pk)
    context = {'document':document}
    return render(request, 'docs/detail.html', context)