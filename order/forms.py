from django import forms

from accounts.models import User


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', 'f_name', 'l_name', 'address_city', 'address_street')

    phone_number = forms.CharField(label='Client Mobile  ',
                                   widget=forms.TextInput(attrs={'id': 'label_title_form'}))
    f_name = forms.CharField(label='Given Name  ',
                             widget=forms.TextInput(attrs={'id': 'label_title_form'}))

    l_name = forms.CharField(label='Family Name  ',
                             widget=forms.TextInput(attrs={'id': 'label_title_form'}))

    address_city = forms.CharField(label='City  ',
                                   widget=forms.TextInput(attrs={'id': 'label_title_form'}))

    address_street = forms.CharField(label='Street  ',
                                     widget=forms.TextInput(attrs={'id': 'label_title_form'}))

    def validate_unique(self):
        pass


class CouponForm(forms.Form):
    code = forms.CharField(label='', widget=forms.TextInput(
        attrs={'id': 'input_discount', 'placeholder': 'Enter Your Code Discount'}))
