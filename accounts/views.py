from datetime import datetime, timedelta
from random import randint

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from accounts.forms import *
from accounts.models import Otp
from product.models import Category, Product
from utils import sms


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        ctx = {
            'form': self.form_class()
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if otps := Otp.objects.filter(phone_number=cd.get('phone_number')):
                otps.delete()

            rand_code = randint(100000, 999999)
            Otp.objects.create(phone_number=cd.get('phone_number'), code=rand_code)
            sms.send_otp(cd.get('phone_number'), rand_code)
            request.session['user_info'] = {
                'phone_number': cd.get('phone_number'),
                'email': cd.get('email'),
                'password': cd.get('password1')
            }

            messages.add_message(request, 200, 'otp sent : ' + str(rand_code), 'success')
            return redirect('accounts:verify-register')
        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)


class UserRegisterVerifyView(View):
    template_name = 'accounts/verify-register.html'
    form_class = OtpForm

    def get(self, request):
        ctx = {
            'form': self.form_class()

        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        user_info = request.session.get('user_info')
        otp_instance = Otp.objects.filter(phone_number=user_info.get('phone_number')).first()
        form = self.form_class(request.POST)
        if form.is_valid():
            user_code = form.cleaned_data['code']
            if user_code != otp_instance.code:
                messages.add_message(request, 200, 'wrong code', 'danger')
                otp_instance.delete()
                del request.session['user_info']

                return redirect('accounts:register')

            otp_exp = otp_instance.created + timedelta(minutes=2)
            now = datetime.now().astimezone(otp_exp.tzinfo)

            if now > otp_exp:
                messages.add_message(request, 200, 'otp expired', 'danger')
                otp_instance.delete()
                del request.session['user_info']

                return redirect('accounts:register')

            user = User.objects.create_user(phone_number=user_info.get('phone_number'),
                                            email=user_info.get('email'),
                                            password=user_info.get('password'))

            login(request, user)
            otp_instance.delete()
            del request.session['user_info']

            messages.add_message(request, 200, 'registered successfully', 'success')
            return redirect('home:home')

        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)


class UserLoginView(View):
    template_name = 'accounts/SignInForm.html'
    form_class = UserLoginForm

    def setup(self, request, *args, **kwargs):

        self.next = request.GET.get('next')
        return super(UserLoginView, self).setup(request, *args, **kwargs)

    def get(self, request):
        ctx = {
            'form': self.form_class()
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd.get('phone_number'), password=cd.get('password'))
            if not user:
                messages.add_message(request, 200, ' user or password is wrong')
                return redirect('accounts:login')

            if otps := Otp.objects.filter(phone_number=cd.get('phone_number')):
                otps.delete()

            rand_code = randint(100000, 999999)
            Otp.objects.create(phone_number=cd.get('phone_number'), code=rand_code)
            sms.send_otp(cd.get('phone_number'), rand_code)
            request.session['login_info'] = {
                'phone_number': cd.get('phone_number'),
                'password': cd.get('password'),
                'next': self.next
            }
            messages.add_message(request, 200, 'otp sent : ' + str(rand_code), 'success')
            return redirect('accounts:login_verify')
        ctx = {
            'form': form
        }
        return render(request, self.template_name, ctx)


class UserLoginVerifyView(View):
    form_class = OtpForm
    template_name = 'accounts/verify-register.html'

    def get(self, request):
        ctx = {
            'form': self.form_class()
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        login_info = request.session.get('login_info')
        otp_instance = Otp.objects.filter(phone_number=login_info.get('phone_number')).first()
        form = self.form_class(request.POST)
        if form.is_valid():
            user_code = form.cleaned_data['code']
            if user_code != otp_instance.code:
                messages.add_message(request, 200, 'wrong code', 'danger')
                otp_instance.delete()
                del request.session['login_info']

                return redirect('accounts:login')

            otp_exp = otp_instance.created + timedelta(minutes=2)
            now = datetime.now().astimezone(otp_exp.tzinfo)
            if now > otp_exp:
                messages.add_message(request, 200, 'otp expired', 'danger')
                otp_instance.delete()
                del request.session['login_info']

                return redirect('accounts:login')

            user = authenticate(request, username=login_info.get('phone_number'), password=login_info.get('password'))
            if user:
                login(request, user)
                messages.add_message(request, 200, 'logged in', 'success')
                if next_param := login_info.get('next'):
                    del request.session['login_info']
                    otp_instance.delete()
                    return redirect(next_param)

                del request.session['login_info']
                otp_instance.delete()
                return redirect('home:home')

            messages.add_message(request, 200, 'user or password wrong', 'danger')

            return redirect('accounts:login')

        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)


class UserLogOut(View):
    def get(self, request):
        logout(request)

        messages.add_message(request, 200, 'logged out', 'info')

        return redirect('home:home')


class UserResetPasswordView(auth_views.PasswordResetView):
    template_name = 'accounts/password-reset-form.html'
    success_url = reverse_lazy('accounts:done')
    email_template_name = 'accounts/password-reset-email.html'


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password-reset-done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password-reset-confirm.html'
    success_url = reverse_lazy('accounts:reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password-reset-complete.html'


class UserChangePasswordView(View):
    form_class = UserChangePasswordForm
    template_name = 'accounts/change-password.html'

    def get(self, request):
        ctx = {
            'form': self.form_class()
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            if otps := Otp.objects.filter(phone_number=cd.get('phone_number')):
                otps.delete()

            rand_code = randint(100000, 999999)
            otp = Otp.objects.create(phone_number=cd.get('phone_number'), code=rand_code)
            sms.send_otp(cd.get('phone_number'), rand_code)
            request.session['user_info'] = {
                'phone_number': cd.get('phone_number'),
                'password': cd.get('password'),
            }
            messages.add_message(request, 200, 'otp sent : ' + str(rand_code), 'success')
            return redirect('accounts:change_password_verify')
        ctx = {
            'form': form
        }
        return render(request, self.template_name, ctx)


class UserChangePasswordVerifyView(View):
    form_class = OtpForm
    template_name = 'accounts/change-password-verify.html'

    def get(self, request):
        ctx = {
            'form': self.form_class
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        user_info = request.session.get('user_info')
        otp_instance = Otp.objects.filter(phone_number=user_info.get('phone_number')).first()

        form = self.form_class(request.POST)
        if form.is_valid():
            user_code = form.cleaned_data['code']
            if user_code != otp_instance.code:
                messages.add_message(request, 200, 'wrongggggg code', 'danger')
                otp_instance.delete()
                del request.session['user_info']
                return redirect('accounts:change_password')

            otp_exp = otp_instance.created + timedelta(minutes=2)
            now = datetime.now().astimezone(otp_exp.tzinfo)
            if now > otp_exp:
                messages.add_message(request, 200, 'code is expired', 'danger')
                otp_instance.delete()
                del request.session['user_info']

                return redirect('accounts:change_password')
            return redirect('accounts:create_new_password')


class UserCreateNewPasswordView(View):
    form_class = UserCreateNewPasswordForm
    template_name = 'accounts/create-new-password.html'

    def get(self, request):
        ctx = {
            'form': self.form_class
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        user_info = request.session.get('user_info')
        form = self.form_class(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']

            if pass1 != pass2:
                messages.add_message(request, 200, "password must be matched")
                ctx = {
                    'form': form
                }
                return render(request, self.template_name, ctx)

            u = User.objects.filter(phone_number=user_info.get('phone_number')).first()
            u.set_password(pass1)
            u.save()
            messages.add_message(request, 200, "password has changed", 'success')

            return redirect('accounts:login')

        ctx = {
            'form': form
        }
        return render(request, self.template_name, ctx)


class UserProfileView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        ctx = {
            'products': products,
            'category': Category.objects.filter(available=True),
        }

        return render(request, 'accounts/profile.html', ctx)


class ShowCategoryFromProfile(View):
    template_name = 'product/product_category.html'

    def get(self, request):
        products = Product.objects.filter(available=True)

        ctx = {
            'products': products,
            'category': Category.objects.filter(available=True),
        }

        return render(request, self.template_name, ctx)


class UserUpdatePersonalInfoView(View):
    form_class = UserUpdatePersonalInfoForm
    template_name = 'accounts/profile_update.html'

    def get(self, request):
        ctx = {
            'form': self.form_class(instance=request.user)
        }

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.add_message(request, 200, 'saved', 'success')
            return redirect('accounts:profile')

        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)


class UserUpdateEmailView(View):
    form_class = UserUpdateEmailForm
    template_name = 'accounts/profile_updateEmail.html'

    def get(self, request):
        ctx = {
            'form': self.form_class(instance=request.user)
        }

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.add_message(request, 200, 'saved', 'success')
            return redirect('accounts:profile')

        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)


class UserUpdateMobileView(View):
    form_class = UserUpdateMobileForm
    template_name = 'accounts/profile_updateMobile.html'

    def get(self, request):
        ctx = {
            'form': self.form_class(instance=request.user)
        }

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.add_message(request, 200, 'saved', 'success')
            return redirect('accounts:profile')

        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)


class UserUpdateAddressView(View):
    form_class = UserUpdateAddressForm
    template_name = 'accounts/profile_updateAddress.html'

    def get(self, request):
        ctx = {
            'form': self.form_class(instance=request.user)
        }

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.add_message(request, 200, 'saved', 'success')
            return redirect('accounts:profile')

        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)


class UserPasswordChangeView(View):
    form_class = PasswordChangeForm
    template_name = 'accounts/change-password_from_profile.html'

    def get(self, request):
        ctx = {
            'form': self.form_class(request.user)
        }

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            form.save()

            update_session_auth_hash(request, form.user)

            messages.add_message(request, 200, 'changed', 'success')
            return redirect('accounts:profile')

        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)
