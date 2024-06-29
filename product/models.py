from django.db import models
from django.urls import reverse

from utils.base_model import BaseModel


class Product(models.Model):
    STATUS = (
        ('none', 'None'),
        ('color', 'Color'),
        ('size', 'Size'),
        ('size_color', 'Size_Color_Var'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    desc = models.TextField()
    unit_price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='products/%Y/%m/%d/')
    image_hover = models.ImageField(null=True, blank=True, upload_to='products/%Y/%m/%d/')
    size_length = models.CharField(null=True, blank=True, max_length=255, default=None)
    size_width = models.CharField(null=True, blank=True, max_length=255, default=None)
    size_height = models.CharField(null=True, blank=True, max_length=255, default=None)
    size_weight = models.CharField(null=True, blank=True, max_length=255, default=None)
    size_area = models.CharField(null=True, blank=True, max_length=255, default=None)
    size_surface_density = models.CharField(null=True, blank=True, max_length=255, default=None)
    size_thickness = models.CharField(null=True, blank=True, max_length=255, default=None)
    size_diameter = models.CharField(null=True, blank=True, max_length=255, default=None)
    discount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='none')
    scroll_show = models.BooleanField(default=True)
    dot_show = models.BooleanField(default=False)
    tag = models.ManyToManyField('TagRelated', blank=True, related_name='tags_related_product')
    category = models.ManyToManyField('Category', related_name='category_product', blank=True)
    likers = models.ManyToManyField('accounts.User', blank=True, related_name='pr_liked_products')
    brand = models.ForeignKey('Brand', models.SET_NULL, 'brand_products', null=True)
    total_sale = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def likers_count(self):
        return self.likers.count()

    def check_like(self, user):
        if self.likers.filter(id=user.id).exists():
            return 'fa-solid'

        return 'fa-regular'

    def get_absolute_url(self):
        return reverse('products:product_details', args=(self.id, self.slug))

    @property
    def final_price(self):
        price = self.unit_price
        if self.discount:
            price = (100 - self.discount) * price // 100

        return price

    @property
    def get_total_seen(self):
        return self.seen.all().count()


class MoreImageOfProduct(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='products/%Y/%m/%d/')
    x = models.ForeignKey('Product', models.CASCADE, null=True, blank=True, related_name='products_extra_image')


class ProductDetails(models.Model):
    description_designer = models.TextField(null=True, blank=True)
    goodToKnow = models.TextField(null=True, blank=True)
    material = models.TextField(null=True, blank=True)
    care = models.TextField(null=True, blank=True)
    safety_compliance = models.TextField(null=True, blank=True)
    y = models.ForeignKey('Product', models.CASCADE, null=True, blank=True, related_name='products_details_info')


class Packaging(models.Model):
    pack_length = models.CharField(null=True, blank=True, max_length=255)
    pack_width = models.CharField(null=True, blank=True, max_length=255)
    pack_height = models.CharField(null=True, blank=True, max_length=255)
    pack_weight = models.CharField(null=True, blank=True, max_length=255)
    pack_area = models.CharField(null=True, blank=True, max_length=255)
    pack_diameter = models.CharField(null=True, blank=True, max_length=255)
    package = models.ForeignKey('Product', models.CASCADE, null=True, blank=True, related_name='products_package')


class Color(models.Model):
    name = models.CharField(max_length=100)
    image_variant = models.ImageField(null=True, blank=True, upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return self.name


class TagRelated(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dimension(models.Model):
    dimension = models.CharField(max_length=255)

    def __str__(self):
        return self.dimension


class Variant(models.Model):
    product = models.ForeignKey('Product', models.CASCADE, 'product_vars')
    color = models.ForeignKey('Color', models.SET_NULL, null=True, blank=True, related_name='color_vars')
    dimension = models.ForeignKey('Dimension', models.SET_NULL, null=True, blank=True, related_name='dimension_vars')
    stock = models.PositiveIntegerField(default=0)
    unit_price = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    discount = models.PositiveIntegerField(default=0)
    total_sale = models.PositiveIntegerField(default=0)

    @property
    def final_price(self):
        price = self.unit_price
        if self.discount:
            price = (100 - self.discount) * price // 100

        return price


class Category(models.Model):
    # product = models.ForeignKey('Product', models.CASCADE, null=True, blank=True,related_name= 'product_category')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_comments')
    user = models.ForeignKey('accounts.User', models.CASCADE, 'user_comments')
    title = models.CharField(null=True, blank=True, max_length=255, default=None)
    reply_to = models.ForeignKey('self', models.CASCADE, related_name='replies', null=True, blank=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField()
    accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    likers = models.ManyToManyField('accounts.User', blank=True, related_name='comment_liked')
    likers_reply = models.ManyToManyField('accounts.User', blank=True, related_name='comment_reply_liked')
    dislikers = models.ManyToManyField('accounts.User', blank=True, related_name='comment_disliked')

    def check_comment_like(self, user):
        if self.likers.filter(id=user.id).exists():
            return 'fa-solid'

        return 'fa-regular'

    def check_comment_dislike(self, user):
        if self.dislikers.filter(id=user.id).exists():
            return 'fa-solid'

        return 'fa-regular'

    def check_comment_reply_like(self, user):
        if self.likers_reply.filter(id=user.id).exists():
            return 'fa-solid'

        return 'fa-regular'

    def __str__(self):
        return f'{self.product.name} - {self.user.f_name}'


class Like(models.Model):
    user_liker_product = models.ForeignKey('accounts.User', null=True, on_delete=models.CASCADE, blank=True,
                                           related_name='user_like_products')

    product = models.ForeignKey('Product', blank=True, null=True, related_name='liked_products',
                                on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', blank=True, null=True, related_name='liked_comments',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    liked = models.BooleanField(default=True)


class Brand(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PriceChange(models.Model):
    product = models.ForeignKey('Product', models.CASCADE, 'price_changes', null=True)
    variant = models.ForeignKey('Variant', models.CASCADE, 'v_price_changes', null=True)
    unit_price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.unit_price}'



class ProductSeen(models.Model):
    product = models.ForeignKey('Product', models.CASCADE, 'seen')
    ip = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.ip}'
