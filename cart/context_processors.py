from cart.cart import Cart, VariantCart


def cart_ctx(request):
    return {
        'cart_len': Cart(request).__len__() + VariantCart(request).__len__()
    }
