from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Patient, Doctor, Procedure
from .forms import ContactForm, PatientForm, DoctorForm, ProcedureForm


# ── Dashboard ──────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    """Render the dashboard with summary counts and recent activity."""
    context = {
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'procedure_count': Procedure.objects.filter(is_active=True).count(),
        'recent_patients': Patient.objects.order_by('-created_at')[:5],
        'recent_doctors': Doctor.objects.select_related('department').order_by('-created_at')[:5],
    }
    return render(request, 'dashboard.html', context)


@login_required
def contact_details(request):
    """Display contact information and handle support inquiries from staff users."""
    initial = {
        'name': request.user.get_full_name() or request.user.get_username(),
        'email': request.user.email,
    }
    form = ContactForm(request.POST or None, initial=initial)

    if request.method == 'POST' and form.is_valid():
        messages.success(
            request,
            f"Your {form.cleaned_data['inquiry_type']} request has been recorded. Our team will contact you shortly.",
        )
        return redirect('contact_details')

    return render(request, 'contact_details.html', {'form': form})


@login_required
def about_us(request):
    """Render the about page describing the CRM mission and operating model."""
    return render(request, 'about_us.html')


# ── Patients ───────────────────────────────────────────────────────────────

@login_required
def patient_list(request):
    query = request.GET.get('q', '').strip()
    patients = Patient.objects.all()
    if query:
        patients = patients.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )
    return render(request, 'patients/list.html', {'patients': patients, 'query': query})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/detail.html', {'patient': patient})


@login_required
def patient_create(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        patient = form.save()
        messages.success(request, f'Patient "{patient.full_name}" added successfully.')
        return redirect('patient_detail', pk=patient.pk)
    return render(request, 'patients/form.html', {'form': form, 'title': 'Add Patient'})


@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        messages.success(request, f'Patient "{patient.full_name}" updated successfully.')
        return redirect('patient_detail', pk=patient.pk)
    return render(request, 'patients/form.html', {'form': form, 'title': 'Edit Patient', 'patient': patient})


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        name = patient.full_name
        patient.delete()
        messages.success(request, f'Patient "{name}" deleted.')
        return redirect('patient_list')
    return render(request, 'patients/confirm_delete.html', {'patient': patient})


# ── Doctors ────────────────────────────────────────────────────────────────

@login_required
def doctor_list(request):
    query = request.GET.get('q', '').strip()
    doctors = Doctor.objects.select_related('department').all()
    if query:
        doctors = doctors.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(specialization__icontains=query) |
            Q(license_number__icontains=query)
        )
    return render(request, 'doctors/list.html', {'doctors': doctors, 'query': query})


@login_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor.objects.select_related('department'), pk=pk)
    return render(request, 'doctors/detail.html', {'doctor': doctor})


@login_required
def doctor_create(request):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        doctor = form.save()
        messages.success(request, f'"{doctor.full_name}" added successfully.')
        return redirect('doctor_detail', pk=doctor.pk)
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Add Doctor'})


@login_required
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        messages.success(request, f'"{doctor.full_name}" updated successfully.')
        return redirect('doctor_detail', pk=doctor.pk)
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Edit Doctor', 'doctor': doctor})


@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        name = doctor.full_name
        doctor.delete()
        messages.success(request, f'"{name}" deleted.')
        return redirect('doctor_list')
    return render(request, 'doctors/confirm_delete.html', {'doctor': doctor})


# ── Procedures ─────────────────────────────────────────────────────────────

@login_required
def procedure_list(request):
    query = request.GET.get('q', '').strip()
    procedures = Procedure.objects.select_related('category').all()
    if query:
        procedures = procedures.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )
    return render(request, 'procedures/list.html', {'procedures': procedures, 'query': query})


@login_required
def procedure_detail(request, pk):
    procedure = get_object_or_404(Procedure.objects.select_related('category'), pk=pk)
    return render(request, 'procedures/detail.html', {'procedure': procedure})


@login_required
def procedure_create(request):
    form = ProcedureForm(request.POST or None)
    if form.is_valid():
        procedure = form.save()
        messages.success(request, f'Procedure "{procedure.name}" added successfully.')
        return redirect('procedure_detail', pk=procedure.pk)
    return render(request, 'procedures/form.html', {'form': form, 'title': 'Add Procedure'})


@login_required
def procedure_edit(request, pk):
    procedure = get_object_or_404(Procedure, pk=pk)
    form = ProcedureForm(request.POST or None, instance=procedure)
    if form.is_valid():
        form.save()
        messages.success(request, f'Procedure "{procedure.name}" updated successfully.')
        return redirect('procedure_detail', pk=procedure.pk)
    return render(request, 'procedures/form.html', {'form': form, 'title': 'Edit Procedure', 'procedure': procedure})


@login_required
def procedure_delete(request, pk):
    procedure = get_object_or_404(Procedure, pk=pk)
    if request.method == 'POST':
        name = procedure.name
        procedure.delete()
        messages.success(request, f'Procedure "{name}" deleted.')
        return redirect('procedure_list')
    return render(request, 'procedures/confirm_delete.html', {'procedure': procedure})

