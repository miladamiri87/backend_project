from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from product.filters import ProductsFilter
from product.form import SearchForm
from product.models import *


class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        products = Product.objects.filter(available=True)

        # if product_id and slug:
        #     products = products.filter(category__slug=slug, category_id=id)

        ctx = {
            'products': products,
            # 'products_scroll': products_scroll,
            # 'products_dot': products_dot,
            # 'category': Category.objects.filter(available=True),

        }

        return render(request, self.template_name, ctx)


class AllProducts(View):
    template_name = 'home/all_products.html'

    def get(self, request, product_id=None, slug=None):
        products = Product.objects.filter(available=True)
        # pr = Product.objects.filter(id=product_id, slug=slug).first()
        filters = ProductsFilter(request.GET, queryset=products)
        products = filters.qs
        if search := request.GET.get('search'):
            products = products.filter(Q(name__icontains=search) | Q(desc__icontains=search))
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        url_data = request.GET.copy()
        if 'page' in url_data:
            del url_data['page']

        ctx = {
            'products': products,
            'category': Category.objects.filter(available=True),
            'filters': filters,
            'url_data': urlencode(url_data),
            'search_form': SearchForm(),
            # 'like_class': pr.check_like(request.user),

        }

        return render(request, self.template_name, ctx)
