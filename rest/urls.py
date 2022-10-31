from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('estudo.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
