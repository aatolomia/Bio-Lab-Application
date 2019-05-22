from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^ChemAid/items$', views.items, name="items"),
    url(r'^ChemAid/categories$', views.categories, name="categories"),
    url(r'^ChemAid/delete_item/(\d+)/$', views.delete_item, name="delete_item"),
    #url(r'^approve/(\d+)/$', views.approve, name="approve"),
    url(r'^ChemAid/edit_item/(\d+)/$', views.edit_item, name="edit_item"),
    url(r'^ChemAid/edit_category/(\d+)/$', views.edit_category, name="edit_category"),
    url(r'^ChemAid/delete_category/(\d+)/$', views.delete_category, name="delete_category"),
    #url(r'^borrowing/(\d+)/$', views.borrowing, name="borrowing"),
    url(r'^ChemAid/approvereturn$', views.approvereturn, name="approvereturn"),
    url(r'^ChemAid/request$', views.request, name="request"),
    url(r'^ChemAid/borrow$',views.options, name="options"),
    url(r'^ChemAid/borrow/(\d+)/$', views.borrow, name="borrow"),
    url(r'^ChemAid/cancel/(\d+)/$', views.cancel, name="cancel"), 
]
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)