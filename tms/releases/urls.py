# Django
from django.urls import path
# Local
from releases import views

urlpatterns = [
    path('release/', views.ReleaseOverviewView.as_view(), name='release_overview'),
    path('release/<int:pk>', views.ReleaseDetailView.as_view(), name='release_detail'),
    path('release/create/', views.ReleaseCreateView.as_view(), name='create_release'),
    path('release/<int:pk>/update', views.ReleaseUpdateView.as_view(), name='update_release'),
    path('release/<int:pk>/read', views.ReleaseReadView.as_view(), name='read_release'),
    path('release/<int:pk>/delete', views.ReleaseDeleteView.as_view(), name='delete_release')

]
