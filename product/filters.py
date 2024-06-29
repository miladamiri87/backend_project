import django_filters
from django import forms


from product.models import Brand


class ProductsFilter(django_filters.FilterSet):
    SORT_PRICE = (
        ('exp', 'expensive'),
        ('chp', 'cheapest'),
    )

    price1 = django_filters.NumberFilter(field_name='unit_price', lookup_expr='gte', label='Price from')
    price2 = django_filters.NumberFilter(field_name='unit_price', lookup_expr='lte', label='Price to')
    sort_price = django_filters.ChoiceFilter(choices=SORT_PRICE, method='get_sort_price',label="Sort Price")

    brand = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(),
                                                     widget=forms.CheckboxSelectMultiple)

    def get_sort_price(self, queryset, name, value):
        o = 'unit_price' if value == 'chp' else '-unit_price'
        return queryset.order_by(o)
