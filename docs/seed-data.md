# Seed Data Instructions

The `seed_data.py` script at the root of the repository populates the database with realistic sample records so you can explore the CRM immediately after installation.

---

## What the Script Creates

| Entity | Count | Details |
|--------|-------|---------|
| Departments | 3 | Cardiology, Neurology, General Medicine |
| Doctors | 5 | Spread across the three departments |
| Patients | 10 | With varied demographics and contact information |

> **Note:** The script uses `get_or_create` for every record, so running it multiple times is safe — existing records will not be duplicated.

---

## Prerequisites

The database migrations must have been applied before seeding:

```bash
python manage.py migrate
```

---

## Running the Script

From the project root (with your virtual environment activated):

```bash
python seed_data.py
```

### Expected output

```
============================================================
Healthcare CRM - Database Seeding Script
============================================================

[STEP 1] Creating Departments...
  ✓ Cardiology: Created
  ✓ Neurology: Created
  ✓ General Medicine: Created

[STEP 2] Creating Doctors...
  ...

[STEP 3] Creating Patients...
  ...

============================================================
Seeding complete!
============================================================
```

---

## After Seeding

Log in to the CRM at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with your superuser credentials to see the seeded data on the dashboard and in the patient/doctor/procedure lists.

---

## Resetting the Database

To start fresh, delete the SQLite file and re-run migrations and the seed script:

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python seed_data.py
```
