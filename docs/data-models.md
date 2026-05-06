# Data Models

This document describes every Django model in the `apps/core` application, including field definitions, constraints, and relationships.

---

## Table of Contents

- [Department](#department)
- [Doctor](#doctor)
- [Patient](#patient)
- [ProcedureCategory](#procedurecategory)
- [Procedure](#procedure)
- [Entity Relationship Overview](#entity-relationship-overview)

---

## Department

Represents a hospital department that groups doctors by specialty area.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `BigAutoField` | PK, auto | Auto-generated primary key |
| `name` | `CharField(100)` | Unique, required | Display name (e.g. "Cardiology") |
| `head_doctor` | `ForeignKey → Doctor` | Nullable, `SET_NULL` | Optional doctor who leads the department |

**Default ordering:** `['name']`

---

## Doctor

A medical professional registered in the CRM.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `BigAutoField` | PK, auto | Auto-generated primary key |
| `first_name` | `CharField(100)` | Required | Doctor's given name |
| `last_name` | `CharField(100)` | Required | Doctor's family name |
| `gender` | `CharField(1)` | Required, choices | `M` Male · `F` Female · `O` Other |
| `specialization` | `CharField(150)` | Required | Medical specialty (e.g. "Cardiologist") |
| `license_number` | `CharField(50)` | Unique, required | Medical licence identifier |
| `phone` | `CharField(20)` | Required | Contact phone number |
| `email` | `EmailField` | Unique, required | Contact e-mail address |
| `department` | `ForeignKey → Department` | Nullable, `SET_NULL` | Department the doctor belongs to |
| `created_at` | `DateTimeField` | Auto, read-only | Timestamp set on creation |

**Default ordering:** `['last_name', 'first_name']`

**Property `full_name`:** Returns `"Dr. {first_name} {last_name}"`.

---

## Patient

A patient whose records are managed in the CRM.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `BigAutoField` | PK, auto | Auto-generated primary key |
| `first_name` | `CharField(100)` | Required | Patient's given name |
| `last_name` | `CharField(100)` | Required | Patient's family name |
| `date_of_birth` | `DateField` | Required | Patient's date of birth |
| `gender` | `CharField(1)` | Required, choices | `M` Male · `F` Female · `O` Other |
| `blood_group` | `CharField(10)` | Choices, default `Unknown` | `A+`, `A-`, `B+`, `B-`, `AB+`, `AB-`, `O+`, `O-`, `Unknown` |
| `phone` | `CharField(20)` | Required | Primary contact phone number |
| `email` | `EmailField` | Optional | Contact e-mail address |
| `address` | `TextField` | Optional | Mailing / residential address |
| `emergency_contact_name` | `CharField(150)` | Optional | Name of next-of-kin |
| `emergency_contact_phone` | `CharField(20)` | Optional | Phone number for emergency contact |
| `created_at` | `DateTimeField` | Auto, read-only | Timestamp set on creation |

**Default ordering:** `['last_name', 'first_name']`

**Property `full_name`:** Returns `"{first_name} {last_name}"`.

---

## ProcedureCategory

A grouping label for medical procedures (e.g. "Diagnostics", "Surgery").

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `BigAutoField` | PK, auto | Auto-generated primary key |
| `name` | `CharField(100)` | Unique, required | Display name of the category |

**Default ordering:** `['name']`  
**verbose_name_plural:** `Procedure Categories`

---

## Procedure

A medical procedure offered by the facility.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `BigAutoField` | PK, auto | Auto-generated primary key |
| `name` | `CharField(200)` | Required | Human-readable name of the procedure |
| `description` | `TextField` | Optional | Free-text description |
| `category` | `ForeignKey → ProcedureCategory` | Nullable, `SET_NULL` | Grouping category |
| `estimated_duration_minutes` | `PositiveIntegerField` | Required | Expected duration in minutes |
| `base_cost` | `DecimalField(10, 2)` | Required | Starting cost of the procedure |
| `is_active` | `BooleanField` | Default `True` | Whether the procedure appears in the dashboard and registration |
| `created_at` | `DateTimeField` | Auto, read-only | Timestamp set on creation |

**Default ordering:** `['name']`

---

## Entity Relationship Overview

```
Department ──< Doctor       (Department.head_doctor → Doctor, Doctor.department → Department)
ProcedureCategory ──< Procedure
```

- A **Department** can have many **Doctors**; a Doctor optionally belongs to one Department.
- A **Department** optionally has one head Doctor (`head_doctor`).
- A **ProcedureCategory** can contain many **Procedures**; a Procedure optionally belongs to one category.
- **Patients** are currently standalone records (no direct FK to Doctor or Procedure in the data model).
