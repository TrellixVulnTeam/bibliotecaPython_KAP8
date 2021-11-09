"""biblioteca URL Configuration

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
from django.urls import path
from django.urls.conf import include
from catalogo.views import indice
from catalogo.views import libros
from catalogo.views import autores
from catalogo.views import contacto
from catalogo.views import buscar

import debug_toolbar
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name='indice'),
    path('libros/', libros, name='libros'),
    path('autores/', autores, name='autores'),
    path('contacto/', contacto, name='contacto'),
    # path('buscar/', buscar, name='buscar'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('catalogo/', include('catalogo.urls')),
    
]
