from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from .models import Expense
from .forms import ExpenseForm

def index(request):
    if request.method=="POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            new_expense = Expense(amount=form.cleaned_data['amount'], category=form.cleaned_data['category'])
            new_expense.save()
            return redirect('/')
    else: 
        form = ExpenseForm()
    expense_list = Expense.objects.all()
    sum_groceries = Expense.sum_amount("Groceries")
    sum_rent = Expense.sum_amount("Rent")
    sum_other = Expense.sum_amount("Other")
    sum_taxes = Expense.sum_amount("Taxes")
    context = {"form" : form ,
               "obj_list" : expense_list ,
               "sum_gr" : sum_groceries , 
               "sum_rt" : sum_rent, 
               "sum_ot" : sum_other,
               "sum_tx" : sum_taxes}
    return render(request, "mainapp/index.j2", context)

class create_expense(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "mainapp/expense_create.html"

def delete_expense(expense_id):
    try:
        expense = Expense.objects.get(id=expense_id)
        expense.delete()
    except Expense.DoesNotExist:
        raise Http404("Expense does not exist.")
    return redirect('/')
