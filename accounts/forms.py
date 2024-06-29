from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Confirm Password')

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'f_name', 'l_name')

    def clean(self):
        cd = super(UserCreationForm, self).clean()
        password1 = cd.get('password1')
        password2 = cd.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password must be match')


def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])

    if commit:
        user.save()
    return user


class UserLoginForm(forms.Form):
    # myfield = AnyOtherField()
    # captcha = CaptchaField()
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text='for change your password click on <a href =" ../password/"> this link </a>  '
    )

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'f_name', 'l_name', 'last_login', 'password')


class UserRegisterForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_phone_number(self):
        user_phone = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=user_phone).exists():
            raise forms.ValidationError('phone must be match!!')

        return user_phone

    def clean_email(self):
        user_email = self.cleaned_data.get('email')
        if User.objects.filter(email=user_email).exists():
            raise forms.ValidationError('phone must be match!!')

        return user_email

    def clean(self):
        cd = super(UserRegisterForm, self).clean()
        password1 = cd.get('password1')
        password2 = cd.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password must be match!!')


class OtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserChangePasswordForm(forms.Form):
    phone_number = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserCreateNewPasswordForm(forms.Form):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserUpdatePersonalInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('f_name', 'l_name', 'date_birthday')


class UserUpdateEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class UserUpdateMobileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number',)


class UserUpdateAddressForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('address_city', 'address_street')
