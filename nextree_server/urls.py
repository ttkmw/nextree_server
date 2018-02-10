"""nextree_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.schemas import get_schema_view
urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('account.urls')),

    path('topic/',include('topic.urls')),
    path('tema/',include('tema.urls')),
    path('post/',include('post.urls')),

    path('api/auth/token/', obtain_jwt_token),
    path('api/', get_schema_view()),
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

