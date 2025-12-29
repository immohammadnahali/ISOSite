"""
URL configuration for ISOSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("product.urls")),
    path('article/', include("product.urls")),
    path('blog/', include("product.urls")),
    path('category/', include("product.urls")),
    path('contact_us/', include("product.urls")),
    path('course/', include("product.urls")),
    path('error404/', include("product.urls")),
    path('forget_password/', include("product.urls")),
    path('login/', include("product.urls")),
    path('panel_user/', include("product.urls")),
    path('search/', include("product.urls")),
    path('sign_up/', include("product.urls")),
    path('teach/', include("product.urls")),

]
