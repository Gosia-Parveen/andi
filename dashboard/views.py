from django.shortcuts import render, HttpResponse, redirect
from .models import Branch
from .form import BranchForm

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


def branch_edit(request, id):
    branch = Branch.objects.get(id=id)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'br_form.html', {'form': form})


def branch_delete(request, id):
    branch = Branch.objects.get(id=id)
    branch.delete()
    return redirect('branch_list')



def social_icon(request):                                 #social_icon
    return render(request, "social_icon.html")


def interface(request):                                 #interface control
    return render(request, "interface.html")
