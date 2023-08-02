from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_exp')
]