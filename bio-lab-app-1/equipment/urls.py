from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'equipment'

urlpatterns = [
	#/equipment/
	path('', views.equipment, name='bio-app-equipment'),
	
	#/equipment/<equipmenttype_id>/ but i want it to be equipment/glasswares
	url(r'^(?P<Category_id>[0-9]+)/$', views.detail, name='bio-app-detail'),

	#/equipment/<equipmenttype_id>/<equipment_id>/
	url(r'^(?P<Category_id>[0-9]+)/(?P<Item_id>[0-9]+)/$', views.item, name='bio-app-item'),

	#/equipment/<equipmenttype_id>/favorite/
	#url(r'^(?P<EquipmentType_id>[0-9]+)/favorite/$', views.favorite, name='bio-app-favorite'),
]

#path('<int: EquipmentType_id>/', views.detail, name='bio-app-detail'),