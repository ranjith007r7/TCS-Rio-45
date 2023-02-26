"""pro26 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from app26 import views
urlpatterns = [
   path('admin/', admin.site.urls),
   path('home/',views.home),
   path('insert/',views.forms),
   path('final/',views.final),
   path('delete/<int:id>',views.delete),
   path('update/<int:id>',views.update),
   path('index/',views.index),
   path('open/',views.open),
   path('service/',views.service),
   path('gallery/',views.gallery),
   path('contact/',views.contact),
   path('accounts/',include('django.contrib.auth.urls')),
   path('logout/',views.logout),
   path('signup/',views.signup_view)
]
