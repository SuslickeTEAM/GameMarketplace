from django import forms

class PaymentForm(forms.Form):
    amount = forms.FloatField(label='Amount to pay', min_value=0)
    order_number = forms.CharField(label='Order number', max_length=20)