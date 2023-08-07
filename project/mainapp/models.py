from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=True)
    amount = models.IntegerField()
    expense_choices = [
        ("Groceries", "Groceries"),
        ("Rent", "Rent"),
        ("Taxes", "Taxes"),
        ("Other", "Other")
    ]
    category = models.CharField(max_length=10, choices=expense_choices, default="Other")
    def __str__(self):
        return f"{self.amount} spent on {self.category}"
    def get_absolute_url(self):
        return '/'
    def sum_amount(list_exp, category):
        sum = 0
        for i in list_exp:
            if i.category==category:
                sum += i.amount
        return sum
    class Meta:
        ordering = ['-pk']