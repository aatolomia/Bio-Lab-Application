"""biolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from student import views as user_views
from equipment import views as eq
from items import views as it_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('student.urls')),
    path('', user_views.welcome, name='welcome'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('updateProfile/', user_views.updateProfile, name='updateProfile'),
    path('login/', user_views.log_in, name='log_in'),
    path('logout/', user_views.log_out, name='log_out'),
    path('cart/', eq.cart, name='cart'),
    path('equipment/', include('equipment.urls')),
    path('adminsite/', user_views.adminsite, name='adminsite'),
    path('adminlogin/', user_views.adminlogin, name='adminlogin'),
    path('adminhome/',user_views.adminhome, name='adminhome'),
    path('adminprofile/', user_views.adminprofile, name='adminprofile'),
    path('adminlogout/', user_views.adminlogout, name='adminlogout'),
    path('updateAdmin/', user_views.updateAdmin, name='updateAdmin'),
    path('admindetails/', user_views.admindetails, name='admindetails'),
    path('items/',it_views.items,name='items'),
    path('categories/',it_views.categories,name='categories'),
    path('request/', it_views.request, name="request"),
    url(r'^', include('items.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
