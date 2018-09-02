# Django
from django.urls import path
# Local
from projects import views

urlpatterns = [
    path('project/', views.ProjectOverviewView.as_view(), name='project_overview'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', views.ProjectCreateView.as_view(), name='create_project'),
    path('project/<int:pk>/update', views.ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:pk>/read', views.ProjectReadView.as_view(), name='read_project'),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='delete_project')
]
