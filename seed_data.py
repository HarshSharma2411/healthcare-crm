import os
import django
import sys
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcarecrm.settings')
django.setup()

from apps.core.models import Department, Doctor, Patient
from datetime import datetime, timedelta
import random


def seed_database():
    """
    Seed the Healthcare CRM database with sample data.
    Creates 3 departments, 5 doctors across departments, and 10 sample patients.
    """
    print("=" * 60)
    print("Healthcare CRM - Database Seeding Script")
    print("=" * 60)

    # ============================================================================
    # STEP 1: Create Departments
    # ============================================================================
    print("\n[STEP 1] Creating Departments...")

    departments_data = [
        {'name': 'Cardiology'},
        {'name': 'Neurology'},
        {'name': 'General Medicine'},
    ]

    departments = {}
    for dept_data in departments_data:
        dept, created = Department.objects.get_or_create(
            name=dept_data['name']
        )
        departments[dept_data['name']] = dept
        status = "Created" if created else "Already exists"
        print(f"  ✓ {dept_data['name']}: {status}")

    # ============================================================================
    # STEP 2: Create Doctors
    # ============================================================================
    print("\n[STEP 2] Creating Doctors...")

    doctors_data = [
        {
            'first_name': 'James',
            'last_name': 'Johnson',
            'gender': 'M',
            'specialization': 'Cardiology',
            'license_number': 'LIC-001-CAR',
            'phone': '+1-555-0101',
            'email': 'james.johnson@hospital.com',
            'department': 'Cardiology',
        },
        {
            'first_name': 'Sarah',
            'last_name': 'Williams',
            'gender': 'F',
            'specialization': 'Neurology',
            'license_number': 'LIC-002-NEU',
            'phone': '+1-555-0102',
            'email': 'sarah.williams@hospital.com',
            'department': 'Neurology',
        },
        {
            'first_name': 'Michael',
            'last_name': 'Brown',
            'gender': 'M',
            'specialization': 'General Internal Medicine',
            'license_number': 'LIC-003-GEN',
            'phone': '+1-555-0103',
            'email': 'michael.brown@hospital.com',
            'department': 'General Medicine',
        },
        {
            'first_name': 'Emily',
            'last_name': 'Davis',
            'gender': 'F',
            'specialization': 'Cardiology',
            'license_number': 'LIC-004-CAR',
            'phone': '+1-555-0104',
            'email': 'emily.davis@hospital.com',
            'department': 'Cardiology',
        },
        {
            'first_name': 'Robert',
            'last_name': 'Martinez',
            'gender': 'M',
            'specialization': 'Neurology',
            'license_number': 'LIC-005-NEU',
            'phone': '+1-555-0105',
            'email': 'robert.martinez@hospital.com',
            'department': 'Neurology',
        },
    ]

    doctors = {}
    for doctor_data in doctors_data:
        dept_name = doctor_data.pop('department')
        doctor, created = Doctor.objects.get_or_create(
            license_number=doctor_data['license_number'],
            defaults={
                **doctor_data,
                'department': departments[dept_name]
            }
        )
        doctors[f"{doctor_data['first_name']} {doctor_data['last_name']}"] = doctor
        status = "Created" if created else "Already exists"
        print(f"  ✓ Dr. {doctor_data['first_name']} {doctor_data['last_name']} ({dept_name}): {status}")

    # ============================================================================
    # STEP 3: Set Department Heads (optional - assign first doctor from each dept)
    # ============================================================================
    print("\n[STEP 3] Assigning Department Heads...")

    department_heads = {
        'Cardiology': doctors['James Johnson'],
        'Neurology': doctors['Sarah Williams'],
        'General Medicine': doctors['Michael Brown'],
    }

    for dept_name, doctor in department_heads.items():
        dept = departments[dept_name]
        dept.head_doctor = doctor
        dept.save()
        print(f"  ✓ {dept_name} head: Dr. {doctor.first_name} {doctor.last_name}")

    # ============================================================================
    # STEP 4: Create Patients
    # ============================================================================
    print("\n[STEP 4] Creating Patients...")

    patients_data = [
        {
            'first_name': 'John',
            'last_name': 'Anderson',
            'date_of_birth': '1965-03-15',
            'gender': 'M',
            'blood_group': 'O+',
            'phone': '+1-555-1001',
            'email': 'john.anderson@email.com',
            'address': '123 Main St, Springfield, IL 62701',
            'emergency_contact_name': 'Mary Anderson',
            'emergency_contact_phone': '+1-555-2001',
        },
        {
            'first_name': 'Jennifer',
            'last_name': 'Thomas',
            'date_of_birth': '1972-07-22',
            'gender': 'F',
            'blood_group': 'A+',
            'phone': '+1-555-1002',
            'email': 'jennifer.thomas@email.com',
            'address': '456 Oak Ave, Springfield, IL 62702',
            'emergency_contact_name': 'David Thomas',
            'emergency_contact_phone': '+1-555-2002',
        },
        {
            'first_name': 'Robert',
            'last_name': 'Jackson',
            'date_of_birth': '1958-11-08',
            'gender': 'M',
            'blood_group': 'B+',
            'phone': '+1-555-1003',
            'email': 'robert.jackson@email.com',
            'address': '789 Pine Rd, Springfield, IL 62703',
            'emergency_contact_name': 'Susan Jackson',
            'emergency_contact_phone': '+1-555-2003',
        },
        {
            'first_name': 'Patricia',
            'last_name': 'White',
            'date_of_birth': '1980-05-30',
            'gender': 'F',
            'blood_group': 'O-',
            'phone': '+1-555-1004',
            'email': 'patricia.white@email.com',
            'address': '321 Elm St, Springfield, IL 62704',
            'emergency_contact_name': 'James White',
            'emergency_contact_phone': '+1-555-2004',
        },
        {
            'first_name': 'Christopher',
            'last_name': 'Harris',
            'date_of_birth': '1975-09-12',
            'gender': 'M',
            'blood_group': 'AB+',
            'phone': '+1-555-1005',
            'email': 'christopher.harris@email.com',
            'address': '654 Birch Ln, Springfield, IL 62705',
            'emergency_contact_name': 'Angela Harris',
            'emergency_contact_phone': '+1-555-2005',
        },
        {
            'first_name': 'Linda',
            'last_name': 'Martin',
            'date_of_birth': '1968-02-18',
            'gender': 'F',
            'blood_group': 'A-',
            'phone': '+1-555-1006',
            'email': 'linda.martin@email.com',
            'address': '987 Cedar Ct, Springfield, IL 62706',
            'emergency_contact_name': 'Michael Martin',
            'emergency_contact_phone': '+1-555-2006',
        },
        {
            'first_name': 'Daniel',
            'last_name': 'Garcia',
            'date_of_birth': '1982-06-25',
            'gender': 'M',
            'blood_group': 'B-',
            'phone': '+1-555-1007',
            'email': 'daniel.garcia@email.com',
            'address': '147 Maple Dr, Springfield, IL 62707',
            'emergency_contact_name': 'Rosa Garcia',
            'emergency_contact_phone': '+1-555-2007',
        },
        {
            'first_name': 'Barbara',
            'last_name': 'Rodriguez',
            'date_of_birth': '1970-10-02',
            'gender': 'F',
            'blood_group': 'AB-',
            'phone': '+1-555-1008',
            'email': 'barbara.rodriguez@email.com',
            'address': '258 Willow Way, Springfield, IL 62708',
            'emergency_contact_name': 'Carlos Rodriguez',
            'emergency_contact_phone': '+1-555-2008',
        },
        {
            'first_name': 'Matthew',
            'last_name': 'Lee',
            'date_of_birth': '1988-04-14',
            'gender': 'M',
            'blood_group': 'O+',
            'phone': '+1-555-1009',
            'email': 'matthew.lee@email.com',
            'address': '369 Spruce St, Springfield, IL 62709',
            'emergency_contact_name': 'Lisa Lee',
            'emergency_contact_phone': '+1-555-2009',
        },
        {
            'first_name': 'Susan',
            'last_name': 'Taylor',
            'date_of_birth': '1976-12-28',
            'gender': 'F',
            'blood_group': 'A+',
            'phone': '+1-555-1010',
            'email': 'susan.taylor@email.com',
            'address': '741 Ash Ave, Springfield, IL 62710',
            'emergency_contact_name': 'Kevin Taylor',
            'emergency_contact_phone': '+1-555-2010',
        },
    ]

    for patient_data in patients_data:
        # Use email as unique identifier since it's typically unique for patients
        patient, created = Patient.objects.get_or_create(
            email=patient_data['email'],
            defaults=patient_data
        )
        status = "Created" if created else "Already exists"
        print(f"  ✓ {patient_data['first_name']} {patient_data['last_name']} (Blood: {patient_data['blood_group']}): {status}")

    # ============================================================================
    # SUMMARY
    # ============================================================================
    print("\n" + "=" * 60)
    print("Seeding Complete!")
    print("=" * 60)
    print(f"\nDatabase Summary:")
    print(f"  • Departments: {Department.objects.count()}")
    print(f"  • Doctors: {Doctor.objects.count()}")
    print(f"  • Patients: {Patient.objects.count()}")
    print("\n✓ Healthcare CRM database is ready for use!")
    print("=" * 60)


if __name__ == '__main__':
    seed_database()
