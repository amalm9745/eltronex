# Generated by Django 5.0.1 on 2024-03-05 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SellerModel',
            fields=[
                ('seller_create_at', models.DateTimeField(auto_created=True)),
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=50)),
                ('seller_password', models.CharField(max_length=50)),
                ('seller_mobile', models.CharField(max_length=50)),
                ('seller_email', models.CharField(max_length=50)),
                ('seller_status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'seller_details',
            },
        ),
        migrations.CreateModel(
            name='MobileVariantModel',
            fields=[
                ('variant_id', models.AutoField(primary_key=True, serialize=False)),
                ('original_price', models.CharField(default='', max_length=100, null=True)),
                ('selling_price', models.CharField(default='', max_length=100, null=True)),
                ('product_quantity', models.IntegerField(default=1, null=True)),
                ('product_add_date', models.DateField(null=True)),
                ('ram', models.CharField(max_length=50)),
                ('rom', models.CharField(max_length=50)),
                ('display', models.CharField(max_length=100)),
                ('camera', models.CharField(max_length=100)),
                ('battery', models.CharField(max_length=50)),
                ('processor', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.categorymodel')),
            ],
            options={
                'db_table': 'mobile_key_features',
            },
        ),
        migrations.CreateModel(
            name='ProductImgModel',
            fields=[
                ('p_img_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_img', models.ImageField(null=True, upload_to='images/product_images/')),
                ('variant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.mobilevariantmodel')),
            ],
            options={
                'db_table': 'product_images',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('product_desc', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.brand')),
                ('sub_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.sub_categorymodel')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.sellermodel')),
            ],
            options={
                'db_table': 'product_details',
            },
        ),
        migrations.AddField(
            model_name='mobilevariantmodel',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.productmodel'),
        ),
    ]
