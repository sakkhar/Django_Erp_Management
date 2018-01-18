from django.contrib import admin

# Register your models here.
from inventory.models import InventoryLocation, InventoryItem


admin.site.register(InventoryLocation)
admin.site.register(InventoryItem)