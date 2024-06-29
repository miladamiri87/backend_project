from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.forms import UserCreationForm, UserChangeForm
from accounts.models import User, Otp


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('phone_number', 'email', 'f_name', 'l_name', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'is_active')

    fieldsets = (
        (
            None,
            {'fields': ('phone_number', 'email', 'f_name', 'l_name', 'address_city',
                        'address_street', 'date_birthday', 'password')}
        ),
        (
            'Permissions',
            {'fields': ('is_active', 'is_admin', 'last_login')}
        )
    )

    add_fieldsets = ((
                         None,
                         {'fields': ('phone_number', 'email', 'f_name', 'l_name', 'password1', 'password2')}
                     ),
    )

    search_fields = ('phone_number', 'email')
    ordering = ('phone_number',)
    filter_horizontal = ()


class OtpAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Otp, OtpAdmin)
