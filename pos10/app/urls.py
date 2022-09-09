"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',include(('bases.urls','bases'), namespace='bases')),
    path('inv/',include(('inv.urls','inv'), namespace='inv')),
    path('cmp/', include(('cmp.urls', 'cmp'), namespace='cmp')),
    path('fac/', include(('fac.urls', 'fac'), namespace='fac')),
    path('ped/', include(('ped.urls', 'ped'), namespace='ped')),
    path('tca/', include(('tca.urls', 'tca'), namespace='tca')),
    path('inf/', include(('inf.urls', 'tca'), namespace='inf')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('ema/', include(('ema.urls', 'ema'), namespace='ema')),
    path('dte/', include(('dte.urls', 'dte'), namespace='dte')),
    
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
