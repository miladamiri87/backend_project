import uuid
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from cart.cart import Cart, VariantCart
from order.forms import UserInfoForm, CouponForm
from order.models import Order, OrderItem, Coupon
from product.models import Product, Variant, Category
from utils import pg

if pg.PIN == 'sandbox':
    PG_URL = 'https://panel.aqayepardakht.ir/startpay/sandbox'
else:
    PG_URL = 'https://panel.aqayepardakht.ir/startpay/'


class OrderCreateView(LoginRequiredMixin, View):
    form_class = UserInfoForm
    template_name = 'create.html'

    def get(self, request):
        cart = Cart(request)
        variant_cart = VariantCart(request)
        ctx = {
            'cart': cart,
            'variant_cart': variant_cart,
            'form': self.form_class(instance=request.user),
            'category': Category.objects.filter(available=True),

        }

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart = Cart(request)
            var_cart = VariantCart(request)

            order = Order.objects.create(
                user=request.user, phone_number=cd.get('phone_number'), f_name=cd.get('f_name'),
                l_name=cd.get('l_name'), address=cd.get('address')
            )
            #
            for i in cart:
                OrderItem.objects.create(
                    order=order, product_id=i['id'], unit_price=i['price'], quantity=i['quantity']
                )

            for i in var_cart:
                obj = OrderItem.objects.create(
                    order=order, variant_id=i['id'], unit_price=i['price'], quantity=i['quantity']
                )
                obj.product = obj.variant.product
                obj.save()

            return redirect('order:details', order.id)

        ctx = {
            'form': form
        }

        return render(request, self.template_name, ctx)


class OrderDetailsView(LoginRequiredMixin, View):
    form_class = CouponForm
    template_name = 'details_order.html'

    def get(self, request, order_id):
        order = Order.objects.filter(id=order_id).first()

        if Coupon.objects.filter(user_exclude=request.user.id).exists():
            discount_used = Coupon.objects.filter(user_exclude=request.user.id).first().discount
        else:
            discount_used = "0"

        if order:
            ctx = {
                'order': order,
                'discount_used': discount_used,
                'form': self.form_class(),
                'category': Category.objects.filter(available=True),

            }

            return render(request, self.template_name, ctx)

        return redirect('cart:cart')

    def post(self, request, order_id):
        order = Order.objects.filter(id=order_id).first()
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']

            if coupon := Coupon.objects.filter(code__exact=code, active=True,
                                               from_date__lte=datetime.now(), to_date__gte=datetime.now()).first():
                if not coupon.user_exclude.filter(id=request.user.id).exists():
                    order.discount = coupon.discount
                    coupon.user_exclude.add(request.user)
                    order.save()

                    return redirect('order:details', order.id)

            messages.add_message(request, 200, 'coupon not valid', 'warning')
            return redirect('order:details', order.id)

        ctx = {
            'order': order,
            'form': form
        }

        return render(request, self.template_name, ctx)


class StartPayView(View):

    def get(self, request, order_id):
        if order := Order.objects.filter(id=order_id , paid = False).first():
            invoice_id = str(uuid.uuid4())
            order.invoice_id = invoice_id
            order.save()

            data = {
                'amount': order.get_total_price,
                'invoice_id': order.invoice_id
            }

            response = pg.create(data)
            res = response.json()
            print(res)
            if response.status_code == 200 and res.get('status') == 'success':
                return redirect(f'{PG_URL}/{res.get("transid")}')

            err = pg.get_err(res.get('code'))
            order.status = res.get('code')
            order.err = err
            order.save()

            messages.add_message(request, 200, 'Faileddddddd', 'danger')
            return redirect('home:home')

        return render(request, '404.html')


class VerifyPaymentView(View):
    def post(self, request):
        data = request.POST
        if order := Order.objects.filter(invoice_id=data.get('invoice_id')).first():
            login(request, order.user)
            order.trans_id = data.get('transid')
            order.card_number = data.get('cardnumber')
            order.tracking_number = data.get('tracking_number')
            order.bank = data.get('bank')
            order.status = data.get('status')
            order.save()

            if data.get('status') == '1':
                data = {
                    'amount': order.get_total_price,
                    'trans_id': order.trans_id
                }

                response = pg.verify(data)
                res = response.json()

                if response.status_code == 200 and res.get('status') == 'success' and res.get('code') == '1':
                    order.paid = True
                    order.save()

                    items = order.order_items.all()
                    for i in items:
                        if not i.variant:
                            prod = Product.objects.filter(id=i.product.id).first()
                            prod.stock -= i.quantity
                            prod.total_sale += i.quantity
                            prod.save()
                        else:
                            var = Variant.objects.filter(id=i.variant.id).first()
                            var.stock -= i.quantity
                            var.total_sale += i.quantity
                            var.save()

                    ctx = {
                        'order': order
                    }

                    return render(request, 'verify-payment.html', ctx)

                err = pg.get_err(res.get('code'))
                order.status = res.get('code')
                order.err = err
                order.save()

                ctx = {
                    'order': order
                }

                return render(request, 'verify-payment.html', ctx)

            err = pg.get_err(data.get('status'))
            order.status = data.get('status')
            order.err = err
            order.save()
            ctx = {
                'order': order
            }

            return render(request, 'verify-payment.html', ctx)

        return render(request, '404.html')
