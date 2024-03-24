# Generated by Django 5.0.1 on 2024-03-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerApp', '0006_rename_mobilevariantmodel_productvariantmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariantmodel',
            name='apps',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productvariantmodel',
            name='display_size',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productvariantmodel',
            name='launch_year',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productvariantmodel',
            name='operating_system',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productvariantmodel',
            name='sound_output',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productvariantmodel',
            name='battery',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productvariantmodel',
            name='camera',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productvariantmodel',
            name='display',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productvariantmodel',
            name='processor',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productvariantmodel',
            name='ram',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productvariantmodel',
            name='storage',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
