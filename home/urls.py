from django.urls import path
from home import views

app_name = 'home'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    path('all_products/', views.AllProducts.as_view(), name='all_products'),

]