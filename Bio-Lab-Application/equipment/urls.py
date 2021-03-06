from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'equipment'

urlpatterns = [
	#/equipment/
	path('', views.equipment, name='bio-app-equipment'),
	
	#/equipment/<equipmenttype_id>/ but i want it to be equipment/glasswares
	url(r'^(?P<EquipmentType_id>[0-9]+)/$', views.detail, name='bio-app-detail'),

	#/equipment/<equipmenttype_id>/<equipment_id>/
	url(r'^(?P<EquipmentType_id>[0-9]+)/(?P<Equipment_id>[0-9]+)/$', views.item, name='bio-app-item'),
	path('items/', include('items.urls')),
	#/equipment/<equipmenttype_id>/favorite/
	#url(r'^(?P<EquipmentType_id>[0-9]+)/favorite/$', views.favorite, name='bio-app-favorite'),
]

#path('<int: EquipmentType_id>/', views.detail, name='bio-app-detail'),