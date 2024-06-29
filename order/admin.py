from django.contrib import admin

# # from django_jalali.admin.filters import JDateFieldListFilter
# # import django_jalali.admin as jadmin
#
from order.models import *


#
#
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


#
#
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'f_name', 'l_name', 'paid', 'created', 'updated')
    inlines = [OrderItemInline]


#
#
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'active', 'from_date', 'to_date')
    list_editable = ('active',)
    list_filter = ('from_date',)
