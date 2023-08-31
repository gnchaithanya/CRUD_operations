"""
URL configuration for project8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Insert_Topic/',Insert_Topic,name='Insert_Topic'),
    path('Insert_Webpage/',Insert_Webpage,name='Insert_Webpage'),
    path('Insert_AR/',Insert_AR,name='Insert_AR'),
    path('display_Topic/',display_Topic,name='display_Topic'),
    path('display_Webpage/',display_Webpage,name='display_Webpage'),
    path('display_AR/',display_AR,name='display_AR'),
    path('Update_Webpage/',Update_Webpage,name='Update_Webpage'),
    path('delete_Webpage/',delete_Webpage,name='delete_Webpage'),

]
