# Django
from django.urls import path
# Local
from projects import views

urlpatterns = [
    path('', views.Index.as_view(), name='dashboard'),
    path('my_work/', views.Index.as_view(), name='my_work'),
    path('project/', views.ProjectOverviewView.as_view(), name='project_overview'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', views.ProjectCreateView.as_view(), name='create_project'),
    path('project/update/<int:pk>', views.ProjectUpdateView.as_view(), name='update_project'),
    path('project/read/<int:pk>', views.ProjectReadView.as_view(), name='read_project'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='delete_project')
]
