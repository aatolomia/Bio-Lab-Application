from django.contrib import admin
from .models import EquipmentType, Equipment, Cart

admin.site.register(EquipmentType)
admin.site.register(Equipment)
admin.site.register(Cart)