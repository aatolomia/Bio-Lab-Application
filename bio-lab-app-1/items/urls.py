from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^items$', views.items, name="items"),
    url(r'^categories$', views.categories, name="categories"),
    url(r'^delete_item/(\d+)/$', views.delete_item, name="delete_item"),
    url(r'^approve/(\d+)/$', views.approve, name="approve"),
    url(r'^edit_item/(\d+)/$', views.edit_item, name="edit_item"),
    url(r'^edit_category/(\d+)/$', views.edit_category, name="edit_category"),
    url(r'^delete_category/(\d+)/$', views.delete_category, name="delete_category"),
    url(r'^borrow$', views.borrow, name="borrow"),
    url(r'^approvereturn$', views.approvereturn, name="approvereturn"),
    url(r'^request$', views.request, name="request"),
]
	
	