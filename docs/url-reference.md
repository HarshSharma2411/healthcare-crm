# URL / Endpoint Reference

All routes are served by the `apps.core` application and mounted at the root (`/`) of the project.  
Authentication is required for every route **except** the login and logout routes listed immediately below — unauthenticated requests to all other routes are redirected to `/login/`.

---

## Authentication Routes

These routes are provided by `django.contrib.auth` and are the only routes accessible without authentication.

| Method | Path | Description |
|--------|------|-------------|
| GET / POST | `/login/` | Staff login form |
| GET / POST | `/logout/` | Logs the current user out and redirects to `/login/` |

---

## Dashboard

| Method | Path | View | Description |
|--------|------|------|-------------|
| GET | `/` | `dashboard` | Summary statistics (patient/doctor/procedure counts), recent patients and doctors, and the list of active procedures |

---

## Patients

| Method | Path | View | Description |
|--------|------|------|-------------|
| GET | `/patients/` | `patient_list` | Paginated list of all patients; supports `?q=` search by name, phone, or e-mail |
| GET | `/patients/<id>/` | `patient_detail` | Detail view for a single patient |
| GET / POST | `/patients/add/` | `patient_create` | Form to register a new patient; `POST` creates the record and redirects to the detail page |
| GET / POST | `/patients/<id>/edit/` | `patient_edit` | Form to update an existing patient; `POST` saves the changes and redirects to the detail page |
| GET / POST | `/patients/<id>/delete/` | `patient_delete` | Confirmation page; `POST` deletes the record and redirects to the patient list |

---

## Doctors

| Method | Path | View | Description |
|--------|------|------|-------------|
| GET | `/doctors/` | `doctor_list` | List of all doctors; supports `?q=` search by name, specialization, or licence number |
| GET | `/doctors/<id>/` | `doctor_detail` | Detail view for a single doctor |
| GET / POST | `/doctors/add/` | `doctor_create` | Form to register a new doctor; `POST` creates the record and redirects to the detail page |
| GET / POST | `/doctors/<id>/edit/` | `doctor_edit` | Form to update an existing doctor; `POST` saves the changes and redirects to the detail page |
| GET / POST | `/doctors/<id>/delete/` | `doctor_delete` | Confirmation page; `POST` deletes the record and redirects to the doctor list |

---

## Procedures

| Method | Path | View | Description |
|--------|------|------|-------------|
| GET | `/procedures/` | `procedure_list` | List of all procedures; supports `?q=` search by name, description, or category |
| GET | `/procedures/<id>/` | `procedure_detail` | Detail view for a single procedure |
| GET / POST | `/procedures/add/` | `procedure_create` | Form to create a new procedure; `POST` creates the record and redirects to the detail page |
| GET / POST | `/procedures/<id>/edit/` | `procedure_edit` | Form to update an existing procedure; `POST` saves the changes and redirects to the detail page |
| GET / POST | `/procedures/<id>/delete/` | `procedure_delete` | Confirmation page; `POST` deletes the record and redirects to the procedure list |

---

## Informational Pages

| Method | Path | View | Description |
|--------|------|------|-------------|
| GET | `/about-us/` | `about_us` | Static page describing the CRM mission and operating model |
| GET / POST | `/contact-details/` | `contact_details` | Contact / support inquiry form pre-filled with the current user's name and e-mail |

---

## Admin Panel

| Path | Description |
|------|-------------|
| `/admin/` | Django admin interface (superuser access required — see [admin-panel.md](admin-panel.md)) |

---

## Search Behaviour

The `?q=` query parameter on list views filters results using case-insensitive `ILIKE` (SQLite `LIKE`) matching across the fields listed below.

| Resource | Searchable fields |
|----------|------------------|
| Patients | `first_name`, `last_name`, `phone`, `email` |
| Doctors | `first_name`, `last_name`, `specialization`, `license_number` |
| Procedures | `name`, `description`, `category__name` |
