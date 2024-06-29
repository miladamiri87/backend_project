from product.models import Product, Variant

CART_SESSION_ID = 'cart'
VARIANT_CART_SESSION_ID = 'var_cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        if not self.session.get(CART_SESSION_ID):
            self.session[CART_SESSION_ID] = {}

        self.cart = self.session.get(CART_SESSION_ID)

    def __len__(self, ):
        # return quantity
        return sum(
            1 for i in self.cart.values()
        )

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for p in products:
            cart[str(p.id)]['product'] = p.name
            cart[str(p.id)]['url'] = p.get_absolute_url()
            cart[str(p.id)]['id'] = p.id

        for item in cart.values():
            item['total_price'] = item['quantity'] * int(item['price'])
            yield item

    def save(self):
        self.session.modified = True

    def add(self, product, quantity):
        p_id = str(product.id)
        if p_id not in self.cart:
            self.cart[p_id] = {'quantity': 0, 'price': str(product.final_price)}

        if self.cart[p_id]['quantity'] + quantity > product.stock:
            return False

        self.cart[p_id]['quantity'] += quantity
        self.save()
        return True

    def remove(self, product, quantity=None):
        product_id = str(product.id)
        if product_id in self.cart:
            if not quantity:
                del self.cart[product_id]
                self.save()
            else:
                if self.cart[product_id]['quantity'] > 1:
                    self.cart[product_id]['quantity'] -= quantity
                    self.save()
                else:
                    self.remove(product)

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

    @property
    def get_total_price(self):
        return sum(
            i['quantity'] * int(i['price']) for i in self.cart.values()
        )


class VariantCart:
    def __init__(self, request):
        self.session = request.session
        if not self.session.get(VARIANT_CART_SESSION_ID):
            self.session[VARIANT_CART_SESSION_ID] = {}

        self.variant_cart = self.session[VARIANT_CART_SESSION_ID]

    def __len__(self):
        return sum(
            1 for item in self.variant_cart.values()
        )

    def __iter__(self):
        var_ids = self.variant_cart.keys()
        variants = Variant.objects.filter(id__in=var_ids)
        variant_cart = self.variant_cart.copy()
        for v in variants:
            variant_cart[str(v.id)]['product'] = v.product.name
            if v.color:
                variant_cart[str(v.id)]['color'] = v.color.name
            else:
                variant_cart[str(v.id)]['color'] = '-'
            if v.dimension:
                variant_cart[str(v.id)]['dimension'] = v.dimension.dimension
            else:
                variant_cart[str(v.id)]['dimension'] = '-'
            variant_cart[str(v.id)]['id'] = v.id
            variant_cart[str(v.id)]['url'] = v.product.get_absolute_url()

        for item in variant_cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item

    def save(self):
        self.session.modified = True

    def add(self, variant, quantity):
        variant_id = str(variant.id)
        if variant_id not in self.variant_cart:
            self.variant_cart[variant_id] = {
                'quantity': 0, 'price': str(variant.final_price)
            }

        if self.variant_cart[variant_id]['quantity'] + quantity > variant.stock:
            return False

        self.variant_cart[variant_id]['quantity'] += quantity
        self.save()
        return True

    def remove(self, variant, quantity=None):
        variant_id = str(variant.id)
        if variant_id in self.variant_cart:
            if not quantity:
                del self.variant_cart[variant_id]
                self.save()
            else:
                if self.variant_cart[variant_id]['quantity'] > 1:
                    self.variant_cart[variant_id]['quantity'] -= quantity
                    self.save()
                else:
                    self.remove(variant)

    def clear(self):
        del self.session[VARIANT_CART_SESSION_ID]
        self.save()

    def total_price(self):
        return sum(
            int(item['price']) * int(item['quantity']) for item in self.variant_cart.values()
        )
