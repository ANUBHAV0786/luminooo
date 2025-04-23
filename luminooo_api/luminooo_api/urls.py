"""
URL configuration for luminooo_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include  # added include after putting comma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')), # include the urls from the main app #this line is new and created in this step
    path ('api-auth/', include('rest_framework.urls')) # added in step 7 , this will show us the login link also at our localhost/api/techer this will allow us to use the browsable API and authentication features of the Django REST framework

]
