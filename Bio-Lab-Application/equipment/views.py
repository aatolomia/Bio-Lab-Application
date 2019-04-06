from django.shortcuts import render, get_object_or_404
from .models import EquipmentType, Equipment, Cart

def equipment(request):
	all_equipmentType = EquipmentType.objects.all()
	context = {'all_equipmentType': all_equipmentType}
	return render(request, 'equipment/index.html', context)

def detail(request, EquipmentType_id):
	#equipType = EquipmentType.objects.get(pk=EquipmentType_id)
	equipType = get_object_or_404(EquipmentType, pk=EquipmentType_id)
	return render(request, 'equipment/detail.html', {'equipType': equipType})

def item(request, EquipmentType_id, Equipment_id):
	equipment = get_object_or_404(Equipment, pk=Equipment_id)
	if request.method == 'POST':
		if request.POST.get('user_b') and request.POST.get('name_of_equip'):
			cart = Cart()
			cart.user_b = request.user
			cart.name_of_equip = request.POST.get('name_of_equip')
			cart.num_of_items = request.POST.get('num_of_items')
			cart.siz = request.POST.get('siz')
			#instance = cart.save(commit=False)
			#instance.user_b = request.user
			cart.save()
	return render(request, 'equipment/item.html', {'equipment': equipment})

def cart(request):
	user_b = request.user
	return render(request, 'equipment/cart.html', {'user_b':user_b})
