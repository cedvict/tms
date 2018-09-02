# Django
from django.urls import path
# Local
from test_plans import views

urlpatterns = [
    path('', views.Index.as_view(), name='dashboard'),
    path('test_plan/', views.TestPlanOverviewView.as_view(), name='test_plan_overview'),
    path('test_plan/<int:pk>', views.TestPlanDetailView.as_view(), name='test_plan_detail'),
    path('test_plan/create/', views.TestPlanCreateView.as_view(), name='create_test_plan'),
    path('test_plan/update/<int:pk>', views.TestPlanUpdateView.as_view(), name='update_test_plan'),
    path('test_plan/read/<int:pk>', views.TestPlanReadView.as_view(), name='read_test_plan'),
    path('test_plan/delete/<int:pk>', views.TestPlanDeleteView.as_view(), name='delete_test_plan')
]
