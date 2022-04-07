"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from core.views import main 
from core.views import kos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main),
    path('moskow',main, name="Москва"),
    path('saint-petersburg', main, name='Санкт-Петербург'),
    path('ekb', main, name='Екатеринбург'),
    path('anadyr', main, name='Анадырь'),
    path('voronezh', main, name='Воронеж'),
    path('Kostroma', main, name='Кострома'),
    path('chelabinsk', main, name='Челябинск')
]
