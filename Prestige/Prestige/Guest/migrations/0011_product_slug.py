# Generated by Django 3.0.5 on 2020-04-23 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0010_auto_20200423_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='singleproduct'),
            preserve_default=False,
        ),
    ]