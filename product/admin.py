from django.contrib import admin

from product.models import *


class MoreImageOfProductInlineAdmin(admin.TabularInline):
    model = MoreImageOfProduct
    extra = 0


class ProductDetailsInlineAdmin(admin.StackedInline):
    model = ProductDetails
    extra = 0


class PackagingInlineAdmin(admin.StackedInline):
    model = Packaging
    extra = 0


class VariantInlineAdmin(admin.TabularInline):
    model = Variant
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'unit_price', 'stock', 'discount', 'final_price', 'available', 'get_total_seen')

    search_fields = ('name',)
    list_filter = ('available', 'category')
    inlines = [MoreImageOfProductInlineAdmin, ProductDetailsInlineAdmin, PackagingInlineAdmin, VariantInlineAdmin,

               ]
    # raw_id_fields = ('tag', )
    # raw_id_fields = ('likers', 'category')

    # inlines = [VariantInlineAdmin]
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'created', 'updated', 'is_sub')
    list_display = ('name', 'created', 'updated')

    prepopulated_fields = {
        'slug': ('name',)
    }


class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'created', 'updated', 'accepted')


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'created', 'comment', 'updated', 'liked',)


class PriceChangeAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'variant', 'unit_price')


@admin.register(ProductSeen)
class ProductSeenAdmin(admin.ModelAdmin):
    list_display = ('product', 'ip', 'date')


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)

admin.site.register(Color)
admin.site.register(TagRelated)

admin.site.register(Dimension)
admin.site.register(Brand)
admin.site.register(PriceChange, PriceChangeAdmin)
