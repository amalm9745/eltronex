from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserAddressModel)
admin.site.register(CartModel)
admin.site.register(WishListModel)
admin.site.register(ReviewModel)
admin.site.register(ShoppingOrderModel)

