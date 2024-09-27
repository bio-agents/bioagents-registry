# -*- coding: UTF-8 -*-
from rest_framework import status
from iechor.test_baseobject import BaseTestObject
from iechor.test_datastructure_json import emptyInputAgent, emptyOutputAgent
import json


class TestCreditsInfrastructure(BaseTestObject):

    def test_creditsInfrastructure_correct_1(self):
        """Sending one string as 'creditsInfrastructure'
        Purpose:
                Basic test of successful sending of a string as creditsInfrastructure
        Sent:
                creditsInfrastructure as a string
        Expected outcome:
                Resource registered with the sent string
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_correct_1'
        sent_resource['credits'] = {
            'creditsInfrastructure': [
                'Just a creditsInfrastructure'
            ]
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_creditsInfrastructure_correct_1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_creditsInfrastructure_correct_1'
        expected_resource['credits'] = {
            'creditsInfrastructure': [
                'Just a creditsInfrastructure'
            ],
            'creditsDeveloper': [],
            'creditsContributor': [],
            'creditsInstitution': [],
            'creditsFunding': [],
            'creditsAffiliation': []
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertItemsEqual(expected_resource, received_resource)

    def test_creditsInfrastructure_correct_2(self):
        """Sending two strings as 'creditsInfrastructure'
        Purpose:
                Basic test of successful sending of a string as creditsInfrastructure
        Sent:
                creditsInfrastructure as a string
        Expected outcome:
                Resource registered with the sent array of 2 strings
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_correct_2'
        sent_resource['credits'] = {
            'creditsInfrastructure': [
                'Just a creditsInfrastructure',
                'another creditsInfrastructure'
            ]
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_creditsInfrastructure_correct_2', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_creditsInfrastructure_correct_2'
        expected_resource['credits'] = {
            'creditsInfrastructure': [
                'Just a creditsInfrastructure',
                'another creditsInfrastructure'
            ],
            'creditsDeveloper': [],
            'creditsContributor': [],
            'creditsInstitution': [],
            'creditsFunding': [],
            'creditsAffiliation': []
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertItemsEqual(expected_resource, received_resource)

    def test_creditsInfrastructure_empty_none(self):
        """Sending null/None as 'creditsInfrastructure'
        Purpose:
                What happens when we send None
        Sent:
                None
        Expected outcome:
                Error informing that this field cannot be null/None
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_empty_none'
        sent_resource['credits'] = {
            'creditsInfrastructure': None
        }

        expected_response = {
            'credits': {
                'creditsInfrastructure': [
                    'This field may not be null.'
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get(
            '/agent/test_creditsInfrastructure_empty_none')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_creditsInfrastructure_empty_zero_length(self):
        """Sending string of zero length as 'creditsInfrastructure'
        Purpose:
                What happens when we send empty string (zero length)
        Sent:
                ''
        Expected outcome:
                Error informing that this field cannot be blank
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_empty_zero_length'
        sent_resource['credits'] = {
            'creditsInfrastructure': ''
        }

        expected_response = {
            'credits': {
                'creditsInfrastructure': {
                    'general_errors': [
                        'Expected a list of items but got type "unicode".'
                    ]
                }
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get(
            '/agent/test_creditsInfrastructure_empty_zero_length')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_creditsInfrastructure_300_length(self):
        """Sending 300 times character 'a' as 'creditsInfrastructure'
        Purpose:
                What happens when we send string of max allowed length
        Sent:
                300 times 'a'
        Expected outcome:
                Resource registered with 300 times 'a' as a creditsInfrastructure
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_300_length'
        sent_resource['credits'] = {
            'creditsInfrastructure': [
                300*'a'
            ]
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_creditsInfrastructure_300_length', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_creditsInfrastructure_300_length'
        expected_resource['credits'] = {
            'creditsInfrastructure': [
                300*'a'
            ],
            'creditsDeveloper': [],
            'creditsContributor': [],
            'creditsInstitution': [],
            'creditsFunding': [],
            'creditsAffiliation': []
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertItemsEqual(expected_resource, received_resource)

    def test_creditsInfrastructure_301_length(self):
        """Sending 301 times character 'a' as 'creditsInfrastructure'
        Purpose:
                What happens when we send more characters than allowed
        Sent:
                301 times 'a'
        Expected outcome:
                Error message informing user of the string length limit
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_301_length'
        sent_resource['credits'] = {
            'creditsInfrastructure': [
                301*'a'
            ]
        }

        expected_response = {
            'credits': {
                'creditsInfrastructure': [
                    [
                        'Ensure this field has no more than 300 characters.'
                    ]
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get(
            '/agent/test_creditsInfrastructure_301_length')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_creditsInfrastructure_non_ascii(self):
        """Sending string with non-ascii characters as 'creditsInfrastructure'
        Purpose:
                What happens when we send non-ascii characters
        Sent:
                String with non-ascii characters
        Expected outcome:
                Resource registered with the non-ascii characters
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_non_ascii'
        sent_resource['credits'] = {
            'creditsInfrastructure': [
                'ąęćżźń£ Ø Δ ♥ †'
            ]
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_creditsInfrastructure_non_ascii', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_creditsInfrastructure_non_ascii'
        expected_resource['credits'] = {
            'creditsInfrastructure': [
                'ąęćżźń£ Ø Δ ♥ †'
            ],
            'creditsDeveloper': [],
            'creditsContributor': [],
            'creditsInstitution': [],
            'creditsFunding': [],
            'creditsAffiliation': []
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertItemsEqual(expected_resource, received_resource)

    def test_creditsInfrastructure_array(self):
        """Sending array as 'creditsInfrastructure'
        Purpose:
                What happens when we send wrong type as the field (this case - array of strings and arrays)
        Sent:
                Array with mixed types (strings and arrays)
        Expected outcome:
                Resource registered with stringified array.
        Note:
                Spaces are added to the stringified value.
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_array'
        sent_resource['credits'] = {
            'creditsInfrastructure': ['a', 'b', 'c', ['d']]
        }

        expected_response = {
            'credits': {
                'creditsInfrastructure': [
                    {},
                    {},
                    {},
                    [
                        'Wrong type found, expected unicode/string, got array/list.'
                    ]
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get('/agent/test_creditsInfrastructure_array')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_creditsInfrastructure_dict(self):
        """Sending dictionary as 'creditsInfrastructure'
        Purpose:
                What happens when we send wrong type as the field (this case - dict of mixed types)
        Sent:
                Dictionary with mixed types (strings and arrays)
        Expected outcome:
                Resource registered with stringified dictionary.
        Note:
                Spaces are added to the stringified value.
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_dict'
        sent_resource['credits'] = {
            'creditsInfrastructure': {'a': 'b', 'c': [1, 2, 3]}
        }

        expected_response = {
            'credits': {
                'creditsInfrastructure': {
                    'general_errors': [
                        'Expected a list of items but got type "dict".'
                    ]
                }
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get('/agent/test_creditsInfrastructure_dict')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_creditsInfrastructure_number(self):
        """Sending number as 'creditsInfrastructure'
        Purpose:
                What happens when we send wrong type as the field (this case - number)
        Sent:
                Number
        Expected outcome:
                Resource registered with stringified number.
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_number'
        sent_resource['credits'] = {
            'creditsInfrastructure': 1234567890
        }

        expected_response = {
            'credits': {
                'creditsInfrastructure': {
                    'general_errors': [
                        'Expected a list of items but got type "int".'
                    ]
                }
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get('/agent/test_creditsInfrastructure_number')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_creditsInfrastructure_array_number(self):
        """Sending array of numbers as 'creditsInfrastructure'
        Purpose:
                What happens when we send wrong type as the field (this case - array of numbers)
        Sent:
                Array of numbers
        Expected outcome:
                Error informing about incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_array_number'
        sent_resource['credits'] = {
            'creditsInfrastructure': [1]
        }

        expected_response = {
            'credits': {
                'creditsInfrastructure': [
                    [
                        'Wrong type found, expected unicode/string, got integer/number.'
                    ]
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get(
            '/agent/test_creditsInfrastructure_array_number')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_creditsInfrastructure_array_dict(self):
        """Sending array of dictionaries as 'creditsInfrastructure'
        Purpose:
                What happens when we send wrong type as the field (this case - array of dictionaries)
        Sent:
                Array of dictionaries
        Expected outcome:
                Registered resource with stringified value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_array_dict'
        sent_resource['credits'] = {
            'creditsInfrastructure': [{'a': 'b', 'c': 5}]
        }

        expected_response = {
            'credits': {
                'creditsInfrastructure': [
                    [
                        'Wrong type found, expected unicode/string, got dictionary/hash.'
                    ]
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get(
            '/agent/test_creditsInfrastructure_array_number')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_creditsInfrastructure_duplicate(self):
        """Sending two identical strings as 'creditsInfrastructure'
        Purpose:
                Checking if the system will remove duplicate elements
        Sent:
                Two identical creditsInfrastructure strings
        Expected outcome:
                Resource registered without the duplicate string
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_creditsInfrastructure_duplicate'
        sent_resource['credits'] = {
            'creditsInfrastructure': [
                'Just a creditsInfrastructure',
                'Just a creditsInfrastructure'
            ]
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_creditsInfrastructure_duplicate', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_creditsInfrastructure_duplicate'
        expected_resource['credits'] = {
            'creditsInfrastructure': [
                'Just a creditsInfrastructure'
            ],
            'creditsDeveloper': [],
            'creditsContributor': [],
            'creditsInfrastructure': [],
            'creditsFunding': [],
            'creditsInstitution': []
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertItemsEqual(expected_resource, received_resource)
