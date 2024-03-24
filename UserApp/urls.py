from django.urls import path,include
from UserApp import views

urlpatterns = [
    path('',views.HomeFun,name='home'),
    path('product/<int:product_id>/<int:variant_id>/', views.product_detail_view, name='product_detail'),
    path('login/',views.loginFun,name='login'),
    path('logout/',views.logout,name="logout"),
    path('addtocart/<int:variant_id>/<str:location>',views.addToCart),
    path('cart/',views.cartFun,name="cart"),
    path('removecartitem/<int:variant_id>/',views.removeCartItem),
    path('myprofile/',views.myProfile,name='myprofile'),
    path('removeaddress/<int:address_id>/',views.removeAddress),
    path('add-to-wishlist/<int:variant_id>/', views.addToWishlist, name='add_to_wishlist'),
    path('wishlist/',views.wishlistView,name='wishlist'),
    path('movetowishlist/<int:variant_id>/',views.moveToWishlist),
    path('removewishlistitem/<int:variant_id>',views.removeWishlistItem),
    path('checkout',views.checkout,name='checkout')

]