from django.contrib import admin
from Guest.models import Product , Reviews , Order, Inventory, Newsletter


# Register your models here.

admin.site.register(Product)
admin.site.register(Reviews)
admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(Newsletter)
