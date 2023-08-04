from django.db import models

# Create your models here.

class Expense(models.Model):
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
    def sum_amount(category):
        list_exp = Expense.objects.filter(category=category)
        return list_exp.aggregate(models.Sum('amount'))['amount__sum']
    class Meta:
        ordering = ['-pk']