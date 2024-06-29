from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from order import views

app_name = 'order'

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='create'),
    path('details/<int:order_id>/', views.OrderDetailsView.as_view(), name='details'),
    path('start-pay/<int:order_id>/', views.StartPayView.as_view(), name='start_pay'),
    path('verify-payment/', csrf_exempt(views.VerifyPaymentView.as_view()), name='verify_payment')
]