from django.shortcuts import render, HttpResponse, redirect
from .models import Branch
from .form import BranchForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def dashboard(request):                              #dashboard
    return render(request, "page1.html")

#def branch(request):                                 #branch
 #   return render(request, "branch.html")

def Other_bank(request):                             #Other_bank
    return render(request, "Other_bank.html")

def deposit(request):                                #deposit
    return render(request, "deposit.html")

def transaction(request):                            #transaction
    return render(request, "transaction.html")

def withdraw(request):                               #withdraw
    return render(request, "withdraw.html")

def user_management(request):                        #user_management
    return render(request, "user_manage.html")


#def br_form(request):                                 #br_form
    #return render(request, "br_form.html")


def branch_list(request):                              # Show all branches
    branches = Branch.objects.all()
    return render(request, 'branch.html', {'branches': branches})


def branch_form(request):                           # Show form and handle POST
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')                 #return to branch
    else:
        form = BranchForm()
    return render(request, 'br_form.html', {'form': form})


def branch_edit(request, id):                             #when you edit the existing branch            
    branch = Branch.objects.get(id=id)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'br_form.html', {'form': form})


def branch_delete(request, id):                             #when you delete the existing branch
    branch = Branch.objects.get(id=id)
    branch.delete()
    return redirect('branch_list')


def social_icon(request):                                 #social_icon
    return render(request, "social_icon.html")


def interface(request):                                 #interface control
    return render(request, "interface.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "index.html")
