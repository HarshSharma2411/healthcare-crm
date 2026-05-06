from django.db import models


class Department(models.Model):
    """A hospital department that groups doctors by specialty area.

    Fields:
        name: Unique display name for the department (e.g. "Cardiology").
        head_doctor: Optional FK to the Doctor who leads the department.
    """

    name = models.CharField(max_length=100, unique=True)
    head_doctor = models.ForeignKey(
        'Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_department',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Doctor(models.Model):
    """A medical professional registered in the CRM.

    Fields:
        first_name / last_name: Doctor's given and family name.
        gender: Single-char choice from GENDER_CHOICES.
        specialization: Medical specialty (e.g. "Cardiologist").
        license_number: Unique medical licence identifier.
        phone: Contact phone number.
        email: Unique contact e-mail address.
        department: Optional FK to the Department the doctor belongs to.
        created_at: Timestamp set automatically on first save.

    Properties:
        full_name: Returns "Dr. <first_name> <last_name>".
    """

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=150)
    license_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='doctors',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'Dr. {self.first_name} {self.last_name}'


class Patient(models.Model):
    """A patient whose records are managed in the CRM.

    Fields:
        first_name / last_name: Patient's given and family name.
        date_of_birth: Patient's date of birth.
        gender: Single-char choice from GENDER_CHOICES.
        blood_group: Blood type choice from BLOOD_GROUP_CHOICES (default "Unknown").
        phone: Primary contact phone number.
        email: Optional contact e-mail address.
        address: Optional mailing / residential address.
        emergency_contact_name: Optional name of next-of-kin or emergency contact.
        emergency_contact_phone: Optional phone number for the emergency contact.
        created_at: Timestamp set automatically on first save.

    Properties:
        full_name: Returns "<first_name> <last_name>".
    """

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('Unknown', 'Unknown'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(
        max_length=10, choices=BLOOD_GROUP_CHOICES, default='Unknown'
    )
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=150, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class ProcedureCategory(models.Model):
    """A grouping label for medical procedures (e.g. "Diagnostics", "Surgery").

    Fields:
        name: Unique display name for the category.
    """

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Procedure Categories'

    def __str__(self):
        return self.name


class Procedure(models.Model):
    """A medical procedure offered by the facility.

    Fields:
        name: Human-readable name of the procedure.
        description: Optional free-text description.
        category: Optional FK to a ProcedureCategory.
        estimated_duration_minutes: Expected length of the procedure in minutes.
        base_cost: Starting cost of the procedure (up to 10 digits, 2 decimal places).
        is_active: When False the procedure is hidden from the dashboard and patient registration.
        created_at: Timestamp set automatically on first save.
    """

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        ProcedureCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='procedures',
    )
    estimated_duration_minutes = models.PositiveIntegerField(
        help_text='Estimated duration in minutes'
    )
    base_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

