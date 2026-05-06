# Contributing to Healthcare CRM

Thank you for taking the time to contribute! Please read the guidelines below before opening a pull request.

---

## Table of Contents

- [Development Setup](#development-setup)
- [Branching Strategy](#branching-strategy)
- [Code Style](#code-style)
- [Writing Tests](#writing-tests)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)

---

## Development Setup

Follow the installation steps in the [README](README.md) to get the project running locally.

---

## Branching Strategy

| Branch pattern | Purpose |
|----------------|---------|
| `main` | Stable, production-ready code |
| `feature/<short-description>` | New features |
| `fix/<short-description>` | Bug fixes |
| `docs/<short-description>` | Documentation-only changes |

Always branch off `main` and open a pull request back to `main`.

---

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Every function and method must include a docstring describing its purpose.
- Keep docstrings concise and focused on purpose, inputs, outputs, or side effects.
- Django models must have class-level docstrings that describe every field.
- Use plain `assert` statements in tests — do not introduce `pytest` or other external test frameworks.

---

## Writing Tests

- Place all tests in `apps/core/tests.py` (or a `tests/` package if the file grows large).
- Every new or updated backend feature (models, views, forms, URLs, admin) must have a corresponding test.
- Use Django's `TestCase` base class.
- Use `assert` statements rather than `self.assert*` methods where possible.

Example test skeleton:

```python
from django.test import TestCase
from django.urls import reverse

class PatientListTests(TestCase):
    """Tests for the patient list view."""

    def test_patient_list_returns_200_for_authenticated_user(self):
        """Verify that the patient list page is accessible to logged-in users."""
        response = self.client.get(reverse('patient_list'))
        assert response.status_code == 200
```

---

## Submitting Changes

1. Fork the repository and create a branch following the naming convention above.
2. Make your changes and ensure all tests pass:
   ```bash
   python manage.py test apps.core
   ```
3. Commit with a clear, imperative message (e.g. `Add patient search by blood group`).
4. Push your branch and open a pull request against `main`.
5. Fill in the pull request template and link any related issues.
6. Address any review feedback before the PR is merged.

---

## Reporting Bugs

Open a GitHub Issue with:

- A clear title and description.
- Steps to reproduce the problem.
- Expected vs. actual behaviour.
- Django version and Python version (`python --version`, `python -m django --version`).
