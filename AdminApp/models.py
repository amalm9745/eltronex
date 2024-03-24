from django.db import models

# Create your models here.
class AdminModel(models.Model):
    admin_id=models.AutoField(primary_key=True)
    admin_name=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
    admin_mobile=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)

    class Meta:
        db_table='admin_details'

    def __str__(self):
        return self.admin_name

class CategoryModel(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table='main_category'

class Sub_CategoryModel(models.Model):
    sub_category_id=models.AutoField(primary_key=True)
    sub_category_name=models.CharField(max_length=50)
    category_id=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name
    
    class Meta:
        db_table='sub_category'








