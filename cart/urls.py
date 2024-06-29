from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:p_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('add-one/<int:p_id>/', views.AddOneToCartView.as_view(), name='add_one_to_cart'),
    path('remove-one/<int:p_id>/', views.RemoveOneFromCartView.as_view(), name='remove_one_from_cart'),
    path('add-var/', views.AddToVarCartView.as_view(), name='add_to_var_cart'),
    path('add-one-var/<int:var_id>/', views.AddOneToVarCartView.as_view(), name='add_one_to_var_cart'),
    path('remove-var/<int:var_id>/', views.RemoveFromVarCartView.as_view(), name='remove_from_var_cart'),
    path('remove-one-var/<int:var_id>/', views.RemoveOneFromVarCartView.as_view(), name='remove_one_from_var_cart'),

]
