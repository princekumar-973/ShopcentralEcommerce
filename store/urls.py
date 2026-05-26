from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',                            views.home,           name='home'),
    path('products/',                   views.product_list,   name='product_list'),
    path('product/<slug:slug>/',        views.product_detail, name='product_detail'),
    path('cart/',                       views.cart_detail,    name='cart_detail'),
    path('cart/add/<int:product_id>/',  views.cart_add,       name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove,  name='cart_remove'),
    # ── NEW ──
    path('order/place/',              views.place_order,   name='place_order'),
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),
    path('contact/', views.contact, name='contact'),
    path('wishlist/toggle/<int:product_id>/', views.wishlist_toggle, name='wishlist_toggle'),
    path('orders/',                   views.my_orders,     name='my_orders'),
]