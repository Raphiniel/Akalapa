from django import forms
from django.forms import ModelForm
from .models import Product, Convo

# create an additem form 
INPUT_CLASSES = 'main'
class NewForm(ModelForm):
    class Meta:
        model = Product
        fields = ("pname", "price", "image")
        labels = {
            'pname': 'Product Name',
            'price': 'Product Price',
            'image':'Product Image',
        }
        widgets = {
            'pname': forms.TextInput(attrs={
                'class':INPUT_CLASSES
                }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
                }),
            'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES
                }),
        }

class MessageForm(ModelForm):
    class Meta:
        model = Convo
        fields = ("message",)
        widgets = {'message': forms.TextInput(attrs={'class': INPUT_CLASSES})},