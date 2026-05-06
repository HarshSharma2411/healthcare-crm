from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from .models import Patient, Doctor, Procedure, ProcedureCategory


class ContactDetailsViewTests(TestCase):
	"""Test coverage for the contact details page workflow."""

	def setUp(self):
		"""Create and authenticate a user for contact page requests."""
		self.user = get_user_model().objects.create_user(
			username='harsh',
			password='test-pass-123',
			email='harsh@example.com',
			first_name='Harsh',
			last_name='Sharma',
		)
		self.client.force_login(self.user)

	def test_contact_details_get_prefills_contact_form(self):
		"""The contact page should render with the logged-in user's details prefilled."""
		response = self.client.get(reverse('contact_details'))

		assert response.status_code == 200
		assert response.context['form'].initial['name'] == 'Harsh Sharma'
		assert response.context['form'].initial['email'] == 'harsh@example.com'

	def test_contact_details_post_redirects_with_success_message(self):
		"""A valid inquiry should redirect back with a success message."""
		response = self.client.post(
			reverse('contact_details'),
			{
				'inquiry_type': 'technical',
				'name': 'Harsh Sharma',
				'email': 'harsh@example.com',
				'subject': 'Access issue',
				'message': 'Unable to load the appointments list.',
			},
			follow=True,
		)

		assert response.status_code == 200
		messages = [message.message for message in get_messages(response.wsgi_request)]
		assert 'technical request has been recorded' in messages[0]

	def test_contact_details_post_shows_validation_errors(self):
		"""An invalid inquiry should keep the user on the page with form errors."""
		response = self.client.post(
			reverse('contact_details'),
			{
				'inquiry_type': 'appointments',
				'name': '',
				'email': 'not-an-email',
				'subject': '',
				'message': '',
			},
		)

		assert response.status_code == 200
		assert response.context['form'].errors

	def test_contact_details_requires_login(self):
		"""Anonymous users should be redirected to login."""
		self.client.logout()

		response = self.client.get(reverse('contact_details'))

		assert response.status_code == 302


class AboutUsViewTests(TestCase):
	"""Test coverage for the about us page."""

	def setUp(self):
		"""Create and authenticate a user for about page requests."""
		self.user = get_user_model().objects.create_user(
			username='about-user',
			password='test-pass-123',
		)
		self.client.force_login(self.user)

	def test_about_us_get_renders_page(self):
		"""The about page should be accessible to authenticated users."""
		response = self.client.get(reverse('about_us'))

		assert response.status_code == 200
		assert b'About Us' in response.content

	def test_about_us_requires_login(self):
		"""Anonymous users should be redirected to login."""
		self.client.logout()

		response = self.client.get(reverse('about_us'))

		assert response.status_code == 302


class DashboardViewTests(TestCase):
	"""Test coverage for the dashboard page, including the procedures quick-register section."""

	def setUp(self):
		"""Create and authenticate a user, and set up sample procedures."""
		self.user = get_user_model().objects.create_user(
			username='dash-user',
			password='test-pass-123',
		)
		self.client.force_login(self.user)

		self.category = ProcedureCategory.objects.create(name='Cardiology')
		self.active_procedure = Procedure.objects.create(
			name='ECG Test',
			category=self.category,
			estimated_duration_minutes=30,
			base_cost='150.00',
			is_active=True,
		)
		self.inactive_procedure = Procedure.objects.create(
			name='Inactive Scan',
			category=self.category,
			estimated_duration_minutes=60,
			base_cost='300.00',
			is_active=False,
		)

	def test_dashboard_renders_for_authenticated_user(self):
		"""The dashboard should be accessible to logged-in users."""
		response = self.client.get(reverse('dashboard'))

		assert response.status_code == 200

	def test_dashboard_requires_login(self):
		"""Anonymous users should be redirected to login."""
		self.client.logout()

		response = self.client.get(reverse('dashboard'))

		assert response.status_code == 302

	def test_dashboard_context_contains_active_procedures(self):
		"""The dashboard context must include only active procedures."""
		response = self.client.get(reverse('dashboard'))

		assert 'active_procedures' in response.context
		procedures_in_context = list(response.context['active_procedures'])
		assert self.active_procedure in procedures_in_context
		assert self.inactive_procedure not in procedures_in_context

	def test_dashboard_shows_procedure_names(self):
		"""Active procedure names should appear in the rendered dashboard HTML."""
		response = self.client.get(reverse('dashboard'))

		assert b'ECG Test' in response.content
		assert b'Inactive Scan' not in response.content

	def test_dashboard_shows_register_patient_button_for_each_procedure(self):
		"""Each active procedure row should contain a Register Patient quick-action link."""
		response = self.client.get(reverse('dashboard'))

		assert b'Register Patient' in response.content
		register_url = reverse('patient_create').encode()
		assert register_url in response.content

	def test_dashboard_procedure_count_matches_active_only(self):
		"""The procedure_count stat on the dashboard should count only active procedures."""
		response = self.client.get(reverse('dashboard'))

		assert response.context['procedure_count'] == 1
