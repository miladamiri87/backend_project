from django.db import models

from utils.base_model import BaseModel

# # from django_jalali.db import models as jmodels


class Order(BaseModel):
    user = models.ForeignKey('accounts.User', models.SET_NULL, 'orders', null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    f_name = models.CharField(max_length=200, null=True, blank=True)
    l_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)
    invoice_id = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=20, null=True)
    err = models.CharField(max_length=255, null=True)
    trans_id = models.CharField(max_length=255, null=True)
    card_number = models.CharField(max_length=20, null=True)
    tracking_number = models.CharField(max_length=255, null=True)
    bank = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.phone_number

    def get_total_price_before_discount(self):
        total_price_before_discount = sum(
            i.get_price for i in self.order_items.all()
        )

        return total_price_before_discount

    @property
    def get_total_price(self):
        total_price = sum(
            i.get_price for i in self.order_items.all()
        )

        if self.discount:
            return (100 - self.discount) * total_price // 100

        return total_price


#

class OrderItem(BaseModel):
    order = models.ForeignKey('Order', models.CASCADE, 'order_items')
    product = models.ForeignKey('product.Product', models.SET_NULL, 'p_order_items', null=True, blank=True)
    variant = models.ForeignKey('product.Variant', models.SET_NULL, 'v_order_items', null=True, blank=True)
    unit_price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)

    #
    def __str__(self):
        return self.order.user.phone_number + self.product.name

    @property
    def get_price(self):
        return self.unit_price * self.quantity


class Coupon(models.Model):
    user_exclude = models.ManyToManyField('accounts.User', blank=True)
    code = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
