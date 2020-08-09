"""happy_paws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve
from django.urls import path
from happy_paws.apps.paws import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AnimalView.as_view(), name='index'),
    path('add_kind', views.KindCreate.as_view(), name='add_kind'),
    path('curator/<int:pk>', views.CuratorDetail.as_view(), name='curator'),
    path('animal/<int:pk>', views.AnimalDetail.as_view(), name='animal')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
