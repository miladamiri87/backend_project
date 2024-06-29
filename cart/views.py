from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from cart.cart import *
from product.models import Product, Variant, Category


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        # quantity =cart.__len__(quantity)
        variant_cart = VariantCart(request)
        all_products = Product.objects.all()

        ctx = {
            'cart': cart,
            'all_products': all_products,
            'variant_cart': variant_cart,
            'category': Category.objects.filter(available=True),

        }

        return render(request, 'cart.html', ctx)


class AddToCartView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            data = {
                'login_required': True
            }
            return JsonResponse(data)
        return super(AddToCartView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        product = Product.objects.filter(id=request.GET.get("product_id")).first()
        quantity = int(request.GET.get("number_order"))
        p_cart = len(Cart(request))
        p_v_cart = len(VariantCart(request))
        p_all = p_cart + p_v_cart
        all_cart = request.session.get(CART_SESSION_ID)

        cart = Cart(request)

        if quantity <= product.stock:
            res = cart.add(product, quantity)
            add_product = True
        else:
            add_product = False
            res = 0

        data = {
            'p_all': p_all,
            'all_cart': all_cart,
            "p_cart": p_cart,
            "add_product": add_product,
            "res": res,
            'quantity': quantity,
            'product_id': request.GET.get("product_id")
        }
        return JsonResponse(data)


class RemoveFromCartView(View):
    def get(self, request, p_id):
        product = Product.objects.filter(id=p_id).first()
        if product:
            cart = Cart(request)
            cart.remove(product)

            messages.add_message(request, 200, 'deleted successfully', 'warning')
            return redirect('cart:cart')

        messages.add_message(request, 200, 'wrong id', 'danger')
        return redirect('cart:cart')


class AddOneToCartView(View):
    def get(self, request, p_id):
        product = Product.objects.filter(id=p_id).first()
        if product:
            cart = Cart(request)
            res = cart.add(product, 1)

            if not res:
                messages.add_message(request, 200, 'more than stock', 'danger')

            return redirect('cart:cart')

        return redirect('cart:cart')


class RemoveOneFromCartView(View):
    def get(self, request, p_id):
        product = Product.objects.filter(id=p_id).first()
        if product:
            cart = Cart(request)
            cart.remove(product, 1)

            return redirect('cart:cart')

        return redirect('cart:cart')


class AddToVarCartView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            data = {
                'login_required': True
            }
            return JsonResponse(data)
        return super(AddToVarCartView, self).dispatch(request, *args, **kwargs)

    def get(self, request):

        variant = Variant.objects.filter(id=request.GET.get("selected_var_id")).first()
        quantity = int(request.GET.get("number_order"))
        all_cart = request.session.get(VARIANT_CART_SESSION_ID)
        p_cart = len(Cart(request))
        p_v_cart = len(VariantCart(request))
        p_all = p_cart + p_v_cart
        cart = VariantCart(request)

        if quantity <= variant.stock:
            res = cart.add(variant, quantity)
            add_product = True
        else:
            add_product = False
            res = 0

        data = {
            'p_all': p_all,
            'all_cart': all_cart,
            "p_cart": p_cart,
            "add_product": add_product,
            "res": res,
            'quantity': quantity,
            'selected_var_id': request.GET.get("selected_var_id")
        }
        return JsonResponse(data)


class RemoveFromVarCartView(View):
    def get(self, request, var_id):
        variant = Variant.objects.filter(id=var_id).first()
        if variant:
            cart = VariantCart(request)
            cart.remove(variant)

            return redirect('cart:cart')

        return redirect('cart:cart')


class RemoveOneFromVarCartView(View):
    def get(self, request, var_id):
        variant = Variant.objects.filter(id=var_id).first()
        if variant:
            cart = VariantCart(request)
            cart.remove(variant, 1)

            return redirect('cart:cart')

        return redirect('cart:cart')


class AddOneToVarCartView(View):
    def get(self, request, var_id):
        variant = Variant.objects.filter(id=var_id).first()
        if variant:
            cart = VariantCart(request)
            res = cart.add(variant, 1)

            if not res:
                messages.add_message(request, 200, 'more than stock', 'danger')

            return redirect('cart:cart')

        return redirect('cart:cart')
