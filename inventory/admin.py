from django.contrib import admin

# Register your models here.
from inventory.models import InventoryLocation, InventoryItem, ItemCrossReference


admin.site.register(InventoryLocation)
admin.site.register(InventoryItem)
admin.site.register(ItemCrossReference)