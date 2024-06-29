import traceback
from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from accounts.models import *
from cart.forms import CartForm
from product.form import CommentForm, SearchForm
from product.models import *
from utils.funcs import get_client_ip


class ProductView(View):
    template_name = 'product/products.html'

    def get(self, request, product_id=None, slug=None):
        products = Product.objects.filter(available=True)
        products_scroll = Product.objects.filter(scroll_show=True)
        products_dot = Product.objects.filter(dot_show=True)
        pr = Product.objects.filter(available=True).all()

        if product_id and slug:
            products = products.filter(category__slug=slug, category_id=id)

        if search := request.GET.get('search'):
            products = products.filter(Q(name__icontains=search) | Q(desc__icontains=search))

        ctx = {
            'products': products,
            'products_scroll': products_scroll,
            'products_dot': products_dot,
            'category': Category.objects.filter(available=True),
            'search_form': SearchForm(),

        }

        return render(request, self.template_name, ctx)


class ProductDetailsView(View):
    template_name = 'product/details.html'
    form_class = CommentForm

    def get(self, request, product_id, slug):
        pr = Product.objects.filter(id=product_id, slug=slug).first()
        all_products = Product.objects.all()

        ip = get_client_ip(request)
        ProductSeen.objects.get_or_create(ip=ip, product=pr)
        total_seen = pr.get_total_seen

        selected_var = None
        if pr.status != 'none':
            selected_var = pr.product_vars.all().first()

        if user_var := request.GET.get('user_var'):
            selected_var = pr.product_vars.filter(id=user_var).first()

        if search := request.GET.get('search'):
            products = pr.filter(Q(name__icontains=search) | Q(desc__icontains=search))

        pr_discount_price = PriceChange.objects.filter(product_id=product_id).all()
        pr_discount_price_varient = PriceChange.objects.filter(variant_id=product_id).all()

        if pr.status != 'none':
            if len(pr_discount_price_varient) >= 2:
                pr_discount_price = pr_discount_price_varient[len(pr_discount_price_varient) - 2].unit_price

        else:
            if len(pr_discount_price) >= 2:
                pr_discount_price = pr_discount_price[len(pr_discount_price) - 2].unit_price
        ctx = {
            'product': pr,
            'selected_var': selected_var,
            'all_products': all_products,
            'comments': Comment.objects.filter(product=pr, accepted=True, is_reply=False),
            'comment_form': self.form_class(),
            'reply_form': self.form_class(),
            'like': Like.objects.filter(product=pr),
            'like_class': pr.check_like(request.user),
            'search_form': SearchForm(),
            'cart_form': CartForm(),
            'category': Category.objects.filter(available=True),
            'total_seen': total_seen,
            'pr_discount_price': pr_discount_price,

        }
        return render(request, self.template_name, ctx)

    @method_decorator(login_required)
    def post(self, request, product_id, slug):
        pr = Product.objects.filter(id=product_id, slug=slug).first()
        form = self.form_class(request.POST)
        if form.is_valid():
            cm = form.save(commit=False)
            cm.user = request.user
            cm.product = pr

            if cm_id := request.GET.get('cm_id'):
                reply_to = Comment.objects.filter(id=cm_id).first()
                cm.reply_to = reply_to
                cm.is_reply = True

            cm.save()
            messages.add_message(request, 200, 'Waite to accept admin', 'success')
            return redirect('products:product_details', pr.id, pr.slug)

        ctx = {
            'product': pr,
            'comments': pr.product_comments.filter(accepted=True),
            'cart_form': CartForm()

        }

        if request.GET.get('cm_id'):
            ctx['comment_form'] = self.form_class()
            ctx['reply_form'] = form
        else:
            ctx['reply_form'] = self.form_class()
            ctx['comment_form'] = form

        return render(request, self.template_name, ctx)


class ProductCategoryView(View):
    template_name = 'product/product_category.html'

    def get(self, request, category_id=None, slug=None):
        products = Product.objects.filter(available=True, category=category_id)

        if search := request.GET.get('search'):
            products = products.filter(
                Q(name__icontains=search) | Q(desc__icontains=search) | Q(tag__name__icontains=search))

        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        url_data = request.GET.copy()
        if 'page' in url_data:
            del url_data['page']

        ctx = {
            'products': products,
            'category': Category.objects.filter(available=True),
            'search_form': SearchForm(),
            'url_data': urlencode(url_data),

        }

        return render(request, self.template_name, ctx)


class ProductLikedView(View):
    template_name = 'product/product_Liked_user.html'

    def get(self, request):
        products = Product.objects.filter(available=True)
        products_liked = Like.objects.filter(liked=True)

        if search := request.GET.get('search'):
            products = products.filter(
                Q(name__icontains=search) | Q(desc__icontains=search) | Q(tag__name__icontains=search))

        paginator = Paginator(products_liked, 10)
        page = request.GET.get('page')
        products_liked = paginator.get_page(page)
        url_data = request.GET.copy()
        if 'page' in url_data:
            del url_data['page']

        ctx = {
            'products': products,
            'products_liked': products_liked,
            'category': Category.objects.filter(available=True),
            'search_form': SearchForm(),
            'search': search,
            'url_data': urlencode(url_data)

        }

        return render(request, self.template_name, ctx)


class ProductLikeView(View):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        like = Like.objects.filter(liked=True, product=product_id)

        if like:
            like.delete()
            product.likers.remove(request.user)

        else:
            product.likers.add(request.user)
            x = Product.objects.filter(id=product_id).first()
            y = User.objects.filter(id=request.user.id).first()
            Like.objects.create(product=x, user_liker_product=y)

        return redirect('products:product_details', product.id, product.slug)


class ProductAjaxLikeView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            data = {
                'login_required': True
            }
            return JsonResponse(data)
        return super(ProductAjaxLikeView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        product = Product.objects.filter(id=request.GET.get("product_id")).first()
        like = Like.objects.filter(liked=True, product=request.GET.get("product_id"))

        if like:
            like.delete()
            product.likers.remove(request.user)
            liked = False

        else:
            product.likers.add(request.user)
            x = Product.objects.filter(id=request.GET.get("product_id")).first()
            y = User.objects.filter(id=request.user.id).first()
            Like.objects.create(product=x, user_liker_product=y)
            liked = True

        data = {
            'liked': liked,
            'likers_count': product.likers_count()

        }

        return JsonResponse(data)


class CommentLikeView(View):

    def get(self, request, comment_id):
        cm = get_object_or_404(Comment, pk=comment_id)
        if cm.dislikers.filter(id=request.user.id).exists():
            cm.dislikers.remove(request.user)

        if cm.likers.filter(id=request.user.id).exists():
            cm.likers.remove(request.user)
        else:
            cm.likers.add(request.user)

        return redirect('products:product_details', cm.product.id, cm.product.slug)


class CommentDisLikeView(View):

    def get(self, request, comment_id):
        cm = get_object_or_404(Comment, id=comment_id)
        if cm.likers.filter(id=request.user.id).exists():
            cm.likers.remove(request.user)

        if cm.dislikers.filter(id=request.user.id).exists():
            cm.dislikers.remove(request.user)
        else:
            cm.dislikers.add(request.user)

        return redirect('products:product_details', cm.product.id, cm.product.slug)


class ReplyLikeView(View):

    def get(self, request, product_id, comment_id):
        product = get_object_or_404(Product, id=product_id)
        rep = get_object_or_404(Comment, id=comment_id)
        if rep.likers_reply.exists():
            rep.likers_reply.remove(request.user)
        else:
            rep.likers_reply.add(request.user)

        return redirect('products:product_details', product.id, product.slug)


class PriceChangeView(View):
    def get(self, request, product_id, slug):
        pr = Product.objects.filter(id=product_id, slug=slug).first()

        pr_discount_price = PriceChange.objects.filter(id=product_id, slug=slug)

        return redirect('products:product_details', pr.product_id, pr.slug)


try:
    ...
except Exception as err:
    f'{err}\n{traceback.format_exc()}'
