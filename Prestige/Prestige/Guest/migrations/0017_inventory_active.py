# Generated by Django 3.0.3 on 2020-05-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0016_cartitem_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='active',
            field=models.BooleanField(default=1),
        ),
    ]
