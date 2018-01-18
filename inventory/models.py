from django.db import models

# Create your models here.
class InventoryLocation(models.Model):
    location_code=models.CharField(max_length=200, unique=True, blank=True, null=True, help_text='Location Code')

    def __unicode__(self):
        return self.location_code


class InventoryItem(models.Model):
    """
    An inventory object
    """

    UOM_CHOICES = (
        ('EA', 'Each'),
        ('LB', 'Pound'),
        ('FT', 'Foot'),
        ('IN', 'Inch'),
        ('C', 'Hundred'),
        ('M', 'Thousand'),
        ('CWT', 'Hundred Weight'),

    )

    PART_TYPES = (
        ('P', 'Purchased'),
        ('M', 'Manufactured'),
    )

    part_number = models.CharField(unique=True, max_length=64)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    part_type = models.CharField(max_length=1, choices=PART_TYPES, default='M')
    stocking_uom = models.CharField(max_length=4, choices=UOM_CHOICES, default='EA')
    purchasing_uom = models.CharField(max_length=4, choices=UOM_CHOICES, default='EA')
    part_weight = models.DecimalField(max_digits=10, decimal_places=10)

    def __unicode__(self):
        return self.part_number


class ItemCrossReference(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.PROTECT)
    cross_reference = models.CharField(max_length=100)

    def __unicode__(self):
        return self.cross_reference

class InventoryTag(models.Model):
    tag