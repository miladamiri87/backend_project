from django.urls import path,include

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('register/verify/', views.UserRegisterVerifyView.as_view(), name='verify-register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('login/verify/', views.UserLoginVerifyView.as_view(), name='login_verify'),
    path('logout/', views.UserLogOut.as_view(), name='logout'),
    path('reset/', views.UserResetPasswordView.as_view(), name='password_reset'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='done'),
    path('reset/confirm/<uidb64>/<token>', views.UserPasswordResetConfirmView.as_view(), name='reset_confirm'),
    path('reset/complete/', views.UserPasswordResetCompleteView.as_view(), name='reset_complete'),
    path('change/', views.UserChangePasswordView.as_view(), name='change_password'),
    path('change/verify/', views.UserChangePasswordVerifyView.as_view(), name='change_password_verify'),
    path('create/new-password/', views.UserCreateNewPasswordView.as_view(), name='create_new_password'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('category/', views.ShowCategoryFromProfile.as_view(), name='profile_to_category'),
    path('profile/update/', views.UserUpdatePersonalInfoView.as_view(), name='profile_update'),
    path('profile/updateEmail/', views.UserUpdateEmailView.as_view(), name='profile_update_email'),
    path('profile/updatemobile/', views.UserUpdateMobileView.as_view(), name='profile_update_mobile'),
    path('profile/updateaddress/', views.UserUpdateAddressView.as_view(), name='profile_update_address'),
    path('profile/password/', views.UserPasswordChangeView.as_view(), name='password_change'),
    # path('captcha/', include('captcha.urls')),

]
