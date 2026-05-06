from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Patients
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),

    # Doctors
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),

    # Procedures
    path('procedures/', views.procedure_list, name='procedure_list'),
    path('procedures/add/', views.procedure_create, name='procedure_create'),
    path('procedures/<int:pk>/', views.procedure_detail, name='procedure_detail'),
    path('procedures/<int:pk>/edit/', views.procedure_edit, name='procedure_edit'),
    path('procedures/<int:pk>/delete/', views.procedure_delete, name='procedure_delete'),
]
