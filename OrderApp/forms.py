from django import forms
from .models import OrderDB, FeedbackDB

weights = [(5, 'Up To 5kg'), (10, 'Up To 10kg'),
           (15, 'Up To 15kg'), (20, 'Up To 20kg')]


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = OrderDB
        fields = ['pick_address', 'pick_phone', 'pick_pincode', 'weight', 'pick_note', 'delivery_address',
                  'delivery_name', 'delivery_phone', 'delivery_pincode', 'delivery_note', 'bill']
        labels = {
            'pick_address': 'Pick up address',
            'pick_phone': '10 digit phone number',
            'pick_pincode': 'pincode',
            'pick_note': '',
            'delivery_address': 'Delivery address',
            'delivery_phone': '10 digit phone number',
            'delivery_pincode': 'pincode',
            'delivery_note': '',
            'delivery_name': 'Name',

        }
        widgets = {
            'pick_address': forms.TextInput(attrs={"placeholder": "Street Name & Locality"}),
            'pick_phone': forms.TextInput(attrs={"maxlength": "10", 'placeholder': '98XXXXXXXX'}),
            'pick_pincode': forms.TextInput(attrs={"maxlength": "6", 'placeholder': '1100XX'}),
            'pick_note': forms.TextInput(attrs={"placeholder": "flat number, floor, building name, street name, landmarks, dimensions, package, fragile, contact name, etc."}),
            'delivery_address': forms.TextInput(attrs={"placeholder": "Drop off Street & Locality "}),
            'delivery_phone': forms.TextInput(attrs={"maxlength": "10", 'placeholder': '98XXXXXXXX'}),
            'delivery_pincode': forms.TextInput(attrs={"maxlength": "6", 'placeholder': '1100XX'}),
            'delivery_note': forms.TextInput(attrs={"placeholder": "flat number, floor, building name, street name, landmarks, dimensions, package, fragile, contact name, etc."}),
            'weight': forms.Select(choices=weights, attrs={}),
            'delivery_name': forms.TextInput(attrs={"placeholder": "Deliver to"}),
            'bill': forms.TextInput(attrs={"readonly": "True"}),
        }



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackDB
        fields = ['order_id', 'feedback']
        widgets = {
            'order_id': forms.HiddenInput(attrs={}),
            'feedback': forms.TextInput(attrs={"placeholder": "Write your feedback here ..."}),
        }
