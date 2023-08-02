from django import forms

class ExpenseForm(forms.Form):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : "Amount"}))
    expense_choices = [
        ("Groceries", "Groceries"),
        ("Rent", "Rent"),
        ("Taxes", "Taxes"),
        ("Other", "Other")
    ]
    category = forms.ChoiceField(choices=expense_choices,
                                widget=forms.Select(attrs={'class' : 'form-control'}))
