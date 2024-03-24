from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SellerModel)
admin.site.register(Brand)
admin.site.register(ProductModel)
admin.site.register(ProductImgModel)
admin.site.register(ProductVariantModel)
