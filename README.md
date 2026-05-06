# Healthcare CRM

A Django-based Customer Relationship Management system for healthcare facilities.  
It lets staff manage **Patients**, **Doctors**, **Procedures**, and **Departments** through a clean web interface and a full Django admin panel.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Development Server](#running-the-development-server)
- [Running Tests](#running-tests)
- [Seeding Sample Data](#seeding-sample-data)
- [Project Structure](#project-structure)
- [Further Documentation](#further-documentation)

---

## Prerequisites

| Requirement | Version |
|-------------|---------|
| Python      | 3.11+   |
| pip         | latest  |

No additional services (databases, caches, queues) are required for local development — the project uses SQLite by default.

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/HarshSharma2411/healthcare-crm.git
cd healthcare-crm

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create a superuser (needed to log in)
python manage.py createsuperuser
```

---

## Running the Development Server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser and log in with the superuser credentials you created above.

---

## Running Tests

```bash
python manage.py test apps.core
```

All tests are located in `apps/core/tests.py`.

---

## Seeding Sample Data

The `seed_data.py` script populates the database with sample departments, doctors, and patients so you can explore the interface immediately.

```bash
python seed_data.py
```

See [docs/seed-data.md](docs/seed-data.md) for full details.

---

## Project Structure

```
healthcare-crm/
├── apps/
│   └── core/               # Main application (models, views, forms, URLs, admin, tests)
├── healthcarecrm/          # Django project settings and root URL configuration
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript, and image assets
├── seed_data.py            # Database seeding script
├── manage.py
└── requirements.txt
```

---

## Further Documentation

| Document | Description |
|----------|-------------|
| [docs/data-models.md](docs/data-models.md) | All Django models with fields and relationships |
| [docs/url-reference.md](docs/url-reference.md) | Full list of URL routes and their behaviour |
| [docs/admin-panel.md](docs/admin-panel.md) | Guide to the Django admin interface |
| [docs/seed-data.md](docs/seed-data.md) | Instructions for populating sample data |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines |
