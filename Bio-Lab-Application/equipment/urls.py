from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'equipment'

urlpatterns = [
	#/equipment/
	path('', views.equipment, name='bio-app-equipment'),
	
	#/equipment/<equipmenttype_id>/ but i want it to be equipment/glasswares
	path('<int:EquipmentType_id>/', views.detail, name='bio-app-detail'),

	#/equipment/<equipmenttype_id>/<equipment_id>/
	path('<int:EquipmentType_id>/<int:Equipment_id>/', views.item, name='bio-app-item'),
]
