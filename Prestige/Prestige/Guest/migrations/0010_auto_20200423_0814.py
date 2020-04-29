# Generated by Django 3.0.5 on 2020-04-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0009_auto_20200423_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(blank=True, help_text="Leave Blank If there's no discount", null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fourth_img',
            field=models.ImageField(blank=True, null=True, upload_to='product/sec_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sec_img',
            field=models.ImageField(blank=True, null=True, upload_to='product/sec_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='third_img',
            field=models.ImageField(blank=True, null=True, upload_to='product/sec_images'),
        ),
    ]
