from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('news/', include('news.urls')),
    path('news/', include('django.contrib.auth.urls')),
    path('test_cases/', include('test_cases.urls')),
    path('test_cases/', include('django.contrib.auth.urls')),
    path('device/', include('devices.urls')),
    path('device/', include('django.contrib.auth.urls')),
    path('project/', include('projects.urls')),
    path('project/', include('django.contrib.auth.urls')),
    path('test_runs/', include('test_runs.urls')),
    path('test_runs/', include('django.contrib.auth.urls')),
    path('', include('dashboard.urls')),
]


