from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path("account/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", views.logout_request, name="logout"),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_exp'),
    path('create/', views.create_expense.as_view(), name="create_expense"),
]