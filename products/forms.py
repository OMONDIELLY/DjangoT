from django import forms


from .models import product
class ProductForm(forms.ModelForm):
    class Meta :
        model = product
        fields = [
            'title',
            'description',
            'price',
            'summary',
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='Your title goes here')
    description  = forms.CharField(required=True)
    price        = forms.CharField(initial=0.0)
    summary      = forms.CharField(required=True)