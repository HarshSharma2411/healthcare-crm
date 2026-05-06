# Django Admin Panel Guide

The Healthcare CRM ships with a fully configured Django admin interface that gives superusers direct access to all database records.

---

## Accessing the Admin Panel

1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) in your browser.
3. Log in with your superuser credentials.  
   If you have not created a superuser yet, run:
   ```bash
   python manage.py createsuperuser
   ```

---

## Registered Models

The following models are registered and manageable through the admin panel.

### Department

| Feature | Details |
|---------|---------|
| List columns | Name, Head Doctor |
| Search | By department name |
| Special | `head_doctor` uses an autocomplete widget |

### Doctor

| Feature | Details |
|---------|---------|
| List columns | Full name, Specialization, Department, Licence number, Phone, Email, Created at |
| Filters | Department, Gender, Specialization |
| Search | First name, Last name, Licence number, Email |
| Fieldsets | **Personal Info** (name, gender) · **Professional Info** (specialization, licence, department) · **Contact** (phone, email) |

### Patient

| Feature | Details |
|---------|---------|
| List columns | Full name, Date of birth, Gender, Blood group, Phone, Email, Created at |
| Filters | Gender, Blood group |
| Search | First name, Last name, Phone, Email |
| Fieldsets | **Personal Info** (name, DOB, gender, blood group) · **Contact** (phone, email, address) · **Emergency Contact** *(collapsible)* |

### ProcedureCategory

| Feature | Details |
|---------|---------|
| Search | By category name |

### Procedure

| Feature | Details |
|---------|---------|
| List columns | Name, Category, Estimated duration (min), Base cost, Active, Created at |
| Filters | Category, Is active |
| Search | Name, Description |
| Special | The **Is active** column is inline-editable directly from the list view |

---

## Common Tasks

### Activating / Deactivating a Procedure

1. Navigate to **Procedures** in the admin sidebar.
2. Find the procedure in the list.
3. Toggle the checkbox in the **Active** column directly in the list, then scroll to the bottom and click **Save**.

### Assigning a Department Head

1. Navigate to **Departments** and click the department you want to edit.
2. Start typing in the **Head Doctor** autocomplete field and select the doctor.
3. Click **Save**.

### Bulk Deleting Records

1. In any list view, tick the checkboxes next to the records you want to remove.
2. Choose **Delete selected …** from the **Action** dropdown.
3. Confirm the deletion on the following page.

---

## Creating Additional Users

Only superusers can log in to the admin panel by default.  
To grant admin access to a non-superuser:

1. Go to **Users** under the **Authentication and Authorization** section.
2. Open the user record.
3. Enable **Staff status** so they can log in to the admin site.
4. Assign the appropriate **Permissions** or **Groups** to control what they can see.
