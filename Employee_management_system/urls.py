"""Employee_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from EMSapp import views
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 
from EMSapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #Company paths 
    path('comp', views.comp, name='comp'),
    path('show', views.show, name='show'),
    path('edit/<str:cName>', views.edit, name='edit'),
    path('update/<str:cName>', views.update, name='update'),
    path('delete/<str:cName>', views.delete, name='delete'), 

    #employee paths
    path('emp', views.emp, name='emp'),
    path('showemp', views.showemp, name='showemp'),
    path('deleteEmp/<str:eFname>', views.deleteEmp, name='deleteEmp'),
    path('editemp/<str:eFname>', views.editemp, name='editemp'), 
    path('updateEmp/<str:eFname>', views.updateEmp, name='updateEmp'),

    #Homepage path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    #inbuilt login path
    path('accounts/', include('django.contrib.auth.urls')),
]
#for Media Storage 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
