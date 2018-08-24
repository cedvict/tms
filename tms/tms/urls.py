from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('console/', include('console.urls')),
    path('admin/', admin.site.urls),
]
