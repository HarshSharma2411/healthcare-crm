from django.contrib import admin
from .models import Department, Doctor, Patient, Procedure, ProcedureCategory


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_doctor')
    search_fields = ('name',)
    autocomplete_fields = ('head_doctor',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'department', 'license_number', 'phone', 'email', 'created_at')
    list_filter = ('department', 'gender', 'specialization')
    search_fields = ('first_name', 'last_name', 'license_number', 'email')
    ordering = ('last_name', 'first_name')
    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'gender')
        }),
        ('Professional Info', {
            'fields': ('specialization', 'license_number', 'department')
        }),
        ('Contact', {
            'fields': ('phone', 'email')
        }),
    )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'blood_group', 'phone', 'email', 'created_at')
    list_filter = ('gender', 'blood_group')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    ordering = ('last_name', 'first_name')
    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'blood_group')
        }),
        ('Contact', {
            'fields': ('phone', 'email', 'address')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone'),
            'classes': ('collapse',),
        }),
    )


@admin.register(ProcedureCategory)
class ProcedureCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'estimated_duration_minutes', 'base_cost', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)

