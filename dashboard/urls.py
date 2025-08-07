from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path("dashboard", views.dashboard, name = 'dashboard'),
    #path("branch", views.branch, name = 'branch'),
    path("Other_bank", views.Other_bank, name = 'Other_bank'),
    path("deposit", views.deposit, name = 'deposit'),
    path("transaction", views.transaction, name = 'transaction'),
    path("withdraw", views.withdraw, name = 'withdraw'),
    path("user_management", views.user_management, name = 'user_management'),
    path('branch', views.branch_list, name='branch_list'),
    path('branch/add', views.branch_form, name='branch_form'),
    path("branch/edit/<int:id>", views.branch_edit, name='branch_edit'),
    path("branch/delete/<int:id>", views.branch_delete, name='branch_delete'),
    path('social_icon', views.social_icon, name='social_icon'),
    path('interface', views.interface, name='interface'),
    path('', views.login_view, name='login'),
]