# Django
from django.urls import path
# Local
from weekly_reports import views

app_name = 'weekly_reports'
urlpatterns = [
    path('', views.WeeklyReportIndex.as_view(), name='device_overview'),
    path('weekly_report/<int:pk>', views.WeeklyReportDetailView.as_view(), name='weekly_report_detail'),
    path('weekly_report/create/', views.WeeklyReportCreateView.as_view(), name='create_weekly_report'),
    path('weekly_report/<int:pk>/update', views.WeeklyReportUpdateView.as_view(), name='update_weekly_report'),
    path('weekly_report/<int:pk>/read', views.WeeklyReportReadView.as_view(), name='read_weekly_report'),
    path('weekly_report/<int:pk>/delete', views.WeeklyReportDeleteView.as_view(), name='delete_weekly_report')
]
