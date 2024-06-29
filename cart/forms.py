from django import forms


class CartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=5, label='',
                                  widget=forms.NumberInput(attrs={'id': 'btn_plus_minus',
                                                                  'placeholder': '0'}))
