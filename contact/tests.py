from rest_framework import status
from rest_framework.test import APITestCase
from .models import Contact

class ContactViewSetTest(APITestCase):
    def setUp(self):
        """
        This method sets up the initial data for the tests.
        It creates valid and invalid data dictionaries that will be used
        to test the `ContactViewSet`.
        """
        self.valid_data = {
            'name': 'Example name',
            'email': 'Examplename@example.com',
            'message': 'This is a test message.'
        }

        self.invalid_data = {
            'name': '',               # Empty name
            'email': 'invalidemail',  # Invalid email format
            'message': ''             # Empty message
        }

    def test_create_contact_success(self):
        """
        Test case for successfully creating a contact.
        It verifies that a valid `POST` request to the `/contact/` endpoint
        with correct data results in a `201 Created` status and that the
        correct response data is returned.
        """
        response = self.client.post('/contact/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check status code
        self.assertIn('message', response.data)                          # Check that the response contains a message
        self.assertEqual(response.data['message'], 'Contact form submitted successfully!')  # Check the message content
        self.assertEqual(Contact.objects.count(), 1)                    # Verify that a new contact was created in the database

    def test_create_contact_failure(self):
        """
        Test case for failing to create a contact.
        It verifies that an invalid `POST` request to the `/contact/` endpoint
        with incorrect data results in a `400 Bad Request` status and that no
        new contact is created in the database.
        """
        response = self.client.post('/contact/', self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Check status code
        self.assertEqual(Contact.objects.count(), 0)                         # Verify that no new contact was created
