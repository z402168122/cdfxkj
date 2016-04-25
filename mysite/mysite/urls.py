"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
import admin
from polls import views

urlpatterns = [
    url( r'^admin/', admin.site.urls ),
    url( r'^$', views.home, {} ),
    url( r'^(?P<path>\w+).html$', views.home, {} ),
    url( r'^products/(?P<product_type>\d+)$', views.product_list ),
    url( r'^products/(?P<product_type>\d+)/(?P<product_id>\d+).html$', views.product_detail ),
    url( r'^abouts$', views.abouts_list, {'about_type':-1} ),
    url( r'^abouts/(?P<about_type>\d+)$', views.abouts_list ),
    url( r'^abouts/(?P<about_type>\d+)/(?P<about_id>\d+).html$', views.abouts_detail ),

    url( r'^supports$', views.supports_list, {'vtype':-1} ),
    url( r'^supports/(?P<vtype>\d+)$', views.supports_list ),
    url( r'^supports/(?P<vtype>\d+)/(?P<vid>\d+).html$', views.supports_detail ),


    url( r'^solutions$', views.solutions_list, {'vtype':-1} ),
    url( r'^solutions/(?P<vtype>\d+)$', views.solutions_list ),
    url( r'^solutions/(?P<vtype>\d+)/(?P<vid>\d+).html$', views.solutions_detail ),

    url( r'^update_img$', views.update_img ),

]
