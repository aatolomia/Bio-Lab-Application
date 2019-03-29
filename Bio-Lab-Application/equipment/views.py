from django.shortcuts import render, get_object_or_404
from .models import EquipmentType, Equipment

def equipment(request):
	all_equipmentType = EquipmentType.objects.all()
	context = {'all_equipmentType': all_equipmentType}
	return render(request, 'equipment/index.html', context)

def detail(request, EquipmentType_id):
	#equipType = EquipmentType.objects.get(pk=EquipmentType_id)
	equipType = get_object_or_404(EquipmentType, pk=EquipmentType_id)
	return render(request, 'equipment/detail.html', {'equipType': equipType})

def item(request, Equipment_id):
	equipment = get_object_or_404(Equipment, pk=Equipment_id)
	return render(request, 'equipment/item.html', {'equipment': equipment})