# -*- coding: UTF-8 -*-
from rest_framework import status
from iechor.test_baseobject import BaseTestObject
from iechor.test_datastructure_json import emptyInputAgent, emptyOutputAgent
import json


class TestiEchorStatus(BaseTestObject):

    def test_iechorStatus_correct_1(self):
        """Sending one of the allowed values as 'iechorStatus'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_correct_1'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': 'IECHOR Core Service'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorStatus_correct_1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorStatus_correct_1'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': 'IECHOR Core Service'
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorStatus_correct_2(self):
        """Sending one of the allowed values as 'iechorStatus'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_correct_2'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': 'IECHOR Named Service'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorStatus_correct_2', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorStatus_correct_2'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': 'IECHOR Named Service'
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorStatus_empty_none(self):
        """Sending null/None as 'iechorStatus'
        Purpose:
                What happens when we send None
        Sent:
                None
        Expected outcome:
                Error informing that this field cannot be null/None
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_empty_none'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': None
        }

        expected_response = {
            'iechorInfo': {
                'iechorStatus': [
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

        response = self.client.get('/agent/test_iechorStatus_empty_none')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorStatus_empty_zero_length(self):
        """Sending string of zero length as 'iechorStatus'
        Purpose:
                What happens when we send empty string (zero length)
        Sent:
                ''
        Expected outcome:
                Error informing that this field cannot be blank
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_empty_zero_length'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': ''
        }

        expected_response = {
            'iechorInfo': {
                'iechorStatus': [
                    'This field may not be blank.'
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
            '/agent/test_iechorStatus_empty_zero_length')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorStatus_invalid(self):
        """Sending incorrect value as 'iechorStatus'
        Purpose:
                Sending incorrect value as iechorNode
        Sent:
                incorrect value for iechorNode
        Expected outcome:
                Error stating incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_invalid'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': 'random string here'
        }

        expected_response = {
            'iechorInfo': {
                'iechorStatus': [
                    'Invalid value: random string here.'
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get('/agent/test_iechorStatus_invalid')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorStatus_array(self):
        """Sending array as 'iechorStatus'
        Purpose:
                What happens when we send wrong type as the field (this case - array of strings and arrays)
        Sent:
                Array with mixed types (strings and arrays)
        Expected outcome:
                Error informing about incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_array'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': ['a', 'b', 'c', ['d']]
        }

        expected_response = {
            'iechorInfo': {
                'iechorStatus': [
                    "Invalid value: [u'a', u'b', u'c', [u'd']]."
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get('/agent/test_iechorStatus_array')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorStatus_dict(self):
        """Sending dictionary as 'iechorStatus'
        Purpose:
                What happens when we send wrong type as the field (this case - dict of mixed types)
        Sent:
                Dictionary with mixed types (strings and arrays)
        Expected outcome:
                Error informing about incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_dict'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': {'a': 'b', 'c': [1, 2, 3]}
        }

        expected_response = {
            'iechorInfo': {
                'iechorStatus': [
                    "Invalid value: {u'a': u'b', u'c': [1, 2, 3]}."
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get('/agent/test_iechorStatus_dict')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorStatus_number(self):
        """Sending number as 'iechorStatus'
        Purpose:
                What happens when we send wrong type as the field (this case - number)
        Sent:
                Number
        Expected outcome:
                Error informing about incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_number'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': 1234567890
        }

        expected_response = {
            'iechorInfo': {
                'iechorStatus': [
                    "Invalid value: 1234567890."
                ]
            }
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), expected_response)

        expected_response = {
            'detail': 'Not found.'
        }

        response = self.client.get('/agent/test_iechorStatus_number')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorStatus_case_sensitive(self):
        """Sending correct value but with wrong case as 'iechorStatus'
        Purpose:
                What happens when we send correct value but with incorrect case (iechor core service instead of IECHOR Core Service)
        Sent:
                Value with correct string but lowercase (iechor core service instead of IECHOR Core Service)
        Expected outcome:
                Resource registered with correct case
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorStatus_case_sensitive'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': 'iechor core service'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorStatus_case_sensitive', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorStatus_case_sensitive'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': 'IECHOR Core Service'
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)
