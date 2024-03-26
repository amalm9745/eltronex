from django.db import models
from AdminApp.models import Sub_CategoryModel,CategoryModel

# Create your models here.
class SellerModel(models.Model):
    seller_id=models.AutoField(primary_key=True)
    seller_name=models.CharField(max_length=50)
    seller_password=models.CharField(max_length=50)
    seller_mobile=models.CharField(max_length=50)
    seller_email=models.CharField(max_length=50)
    seller_create_at=models.DateTimeField(auto_created=True)
    seller_status=models.BooleanField(default=True)
    

    class Meta:
        db_table='seller_details'

    def __str__(self):
        
        return self.seller_name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductModel(models.Model):

    product_id=models.AutoField(primary_key=True)
    product_title=models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    product_desc=models.TextField()
    seller_id=models.ForeignKey(SellerModel,on_delete=models.CASCADE)
    sub_category_id=models.ForeignKey(Sub_CategoryModel,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        db_table='product_details'

    def __str__(self):
        return self.product_title


class ProductVariantModel(models.Model):
    variant_id=models.AutoField(primary_key=True)
    variant_name=models.CharField(max_length=100,null=True)
    original_price=models.CharField(max_length=100,default='',null=True)
    selling_price=models.CharField(max_length=100,default='',null=True)
    product_quantity=models.IntegerField(default=1,null=True)
    product_add_date=models.DateField(null=True)
    color=models.CharField(max_length=100,null=True,default='',blank=True)
    ram=models.CharField(max_length=50,null=True,default='',blank=True)
    storage=models.CharField(max_length=50,null=True,default="",blank=True)
    display=models.CharField(max_length=100,null=True,default="",blank=True)
    camera=models.CharField(max_length=100,null=True,default="",blank=True)
    battery=models.CharField(max_length=50,null=True,default="",blank=True)
    processor=models.CharField(max_length=100,null=True,default="",blank=True)
    operating_system=models.CharField(max_length=100,null=True,default="",blank=True)
    display_size=models.CharField(max_length=50,null=True,default="",blank=True)
    sound_output=models.CharField(max_length=50,null=True,default="",blank=True)
    apps=models.CharField(max_length=100,null=True,default="",blank=True)
    launch_year=models.CharField(max_length=50,null=True,default="",blank=True)
    product_id=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    category_id=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.variant_name
    
    class Meta:
        db_table='mobile_key_features'


class ProductImgModel(models.Model):

    p_img_id=models.AutoField(primary_key=True)
    p_img=models.ImageField(upload_to='images/product_images/',null=True)
    variant_id=models.ForeignKey(ProductVariantModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.variant_id.variant_name
    
    class Meta:
        db_table='product_images'

