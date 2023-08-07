from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from .models import Expense
from .forms import ExpenseForm, SignUpForm, LoginForm, RegisterForm

@login_required
def index(request):
    current_user=request.user
    expense_list = Expense.objects.filter(user_id=current_user.id)
    sum_groceries = Expense.sum_amount(expense_list, "Groceries")
    sum_rent = Expense.sum_amount(expense_list, "Rent")
    sum_other = Expense.sum_amount(expense_list, "Other")
    sum_taxes = Expense.sum_amount(expense_list, "Taxes")
    context = {"obj_list" : expense_list ,
               "sum_gr" : sum_groceries , 
               "sum_rt" : sum_rent, 
               "sum_ot" : sum_other,
               "sum_tx" : sum_taxes}
    return render(request, "mainapp/index.j2", context)

def login_request(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("invalid credentials")
    else:
        form = LoginForm()
    context = {
        "form" : form   
    }
    return render(request, "registration/login.html", context) 

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            hashed_password = make_password(password)
            user = User.objects.filter(username=username)
            if not user.exists():
                new_user = User(username=username, password=hashed_password)
                new_user.save()
                login(request, new_user)
                return redirect("index")
            else:
                return HttpResponse("The user is already exist")
    else:
        form = RegisterForm()
    context = {"form" : form}
    return render(request, "registration/register.html", context)

""" class SignUp(CreateView):
    form_class = SignUpForm
    template_name="registration/register.html"
    success_url = reverse_lazy("index")
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        context = {"form" : SignUpForm}
        return render(request, self.template_name, context) """

@login_required
def logout_request(request):
    logout(request)
    return redirect("index")

class create_expense(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "mainapp/expense_create.html"
    success_url = reverse_lazy("index") 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def delete_expense(request, expense_id):
    try:
        expense = Expense.objects.get(id=expense_id)
        expense.delete()
    except Expense.DoesNotExist:
        raise Http404("Expense does not exist.")
    return redirect('index')