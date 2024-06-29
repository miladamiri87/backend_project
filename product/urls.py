from django.urls import path

from product import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('category_product/<int:category_id>/<slug>/', views.ProductCategoryView.as_view(), name='c_products'),
    path('liked_user_products/', views.ProductLikedView.as_view(), name='liked_user_products'),
    path('details/<int:product_id>/<slug>/', views.ProductDetailsView.as_view(), name='product_details'),
    path('product-like/<int:product_id>', views.ProductLikeView.as_view(), name='product_like'),
    path('product-like/', views.ProductAjaxLikeView.as_view(), name='product_like_ajax'),
    path('comment-like/<int:comment_id>/', views.CommentLikeView.as_view(), name='comment_like'),
    path('comment-dislike/<int:comment_id>/', views.CommentDisLikeView.as_view(), name='comment_dislike'),
    path('comment-reply-like/<int:product_id>/<int:comment_id>/', views.ReplyLikeView.as_view(), name='comment_reply_like'),

]
