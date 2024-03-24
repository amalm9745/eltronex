from django.db import models
from SellerApp.models import ProductModel,ProductVariantModel
# Create your models here.
class UserModel(models.Model):

    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=50)
    user_image=models.ImageField(upload_to='images/user_profile/',null=True,blank=True)
    user_password=models.CharField(max_length=50)
    user_mobile=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=50,null=True,blank=True)
    user_create_at=models.DateTimeField(auto_created=True)
    user_status=models.BooleanField(default=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table='user_details'


class UserAddressModel(models.Model):

    address_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    locality=models.CharField(max_length=50,null=True,blank=True)
    pincode=models.CharField(max_length=50,)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    landmark=models.CharField(max_length=150,null=True,blank=True)
    address_type=models.CharField(max_length=50)
    user_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)

    class Meta:
        db_table='user_addresses'

    def __str__(self):
        return self.user_id.user_name

class CartModel(models.Model):
    cart_id=models.AutoField(primary_key=True)
    quantity=models.IntegerField()
    user_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    variant_id=models.ForeignKey(ProductVariantModel,on_delete=models.CASCADE,null=True,blank=True)

    
    def __str__(self):
        return self.user_id.user_name

    class Meta:
        db_table='user_cart'

class WishListModel(models.Model):
    wishlist_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    variant_id=models.ForeignKey(ProductVariantModel,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user_id.user_name
    
    class Meta:
        db_table='user_wishlist'

class ReviewModel(models.Model):
    review_id=models.AutoField(primary_key=True)
    review_content=models.CharField(max_length=255)
    review_date=models.DateField(auto_created=True)
    review_img1=models.ImageField(upload_to='images/user_review/',null=True)
    user_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    product_id=models.ForeignKey(ProductModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.user_name
    
    class Meta:
        db_table="user_review"

class ShoppingOrderModel(models.Model):
    order_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_created=True)
    user_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    address_id=models.ForeignKey(UserAddressModel,on_delete=models.CASCADE)

    class Meta:
        db_table="user_orders"

    def __str__(self):
        return self.user_id.user_name

# class PaymentModel(models.Model):
#     payment_id=models.AutoField(primary_key=True)
#     payment_type=models.CharField(max_length=50)
#     date=models.DateTimeField()
#     order_id=models.ForeignKey(ShoppingOrderModel,on_delete=models.CASCADE)

#     class Meta:
#         db_table="payment_details"


    
    



