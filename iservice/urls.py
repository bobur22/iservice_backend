from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('calendar/', views.calendar_view, name='calendar'),

    path('employees/', views.employees_view, name='employees'),
    path('employee_delete/<int:id>/', views.employees_delete, name='employee_delete'),
    path('employee_detail/<int:id>/', views.employees_detail_view, name='employees_detail'),

    path('customers/', views.customers_view, name='customers'),
    path('customer_delete/<int:id>/', views.customer_delete, name='customer_delete'),
    path('customer_detail/<int:id>/', views.customers_detail_view, name='customer_detail'),
    path('customers/download/', views.download_customers_excel, name='download_customers_excel'),

    path('locations/', views.locations_view, name='locations'),
    path('locations/download/', views.download_excel, name='download_excel'),

    path('tasks/', views.tasks_view, name='tasks'),
    path('tasks/archive/', views.tasks_archive_view, name='tasks_archive'),
    path('tasks/archive/download/', views.tasks_archive_download_excel, name='t_a_download_excel'),
    path('task_delete/<int:id>/', views.task_delete, name='task_delete'),
    path('task_detail/<int:id>/', views.tasks_detail_view, name='task_detail'),
]
