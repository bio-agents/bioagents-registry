# -*- coding: UTF-8 -*-
from rest_framework import status
from iechor.test_baseobject import BaseTestObject
from iechor.test_datastructure_json import emptyInputAgent, emptyOutputAgent
import json


class TestiEchorNode(BaseTestObject):

    def test_iechorNode_correct_1(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_1'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Denmark'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_1'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_2(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_2'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Czech Republic'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_2', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_2'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Czech Republic',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_3(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_3'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Belgium'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_3', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_3'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Belgium',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_4(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_4'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'EMBL-EBI'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_4', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_4'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'EMBL-EBI',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_5(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_5'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Estonia'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_5', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_5'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Estonia',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_6(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_6'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Finland'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_6', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_6'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Finland',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_7(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_7'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'France'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_7', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_7'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'France',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_8(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_8'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Greece'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_8', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_8'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Greece',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_9(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_9'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Israel'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_9', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_9'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Israel',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_10(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_10'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Italy'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_10', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_10'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Italy',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_11(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_11'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Netherlands'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_11', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_11'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Netherlands',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_12(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_12'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Norway'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_12', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_12'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Norway',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_13(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_13'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Portugal'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_13', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_13'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Portugal',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_14(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_14'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Slovenia'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_14', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_14'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Slovenia',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_15(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_15'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Spain'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_15', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_15'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Spain',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_16(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_16'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Sweden'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_16', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_16'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Sweden',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_17(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_17'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'Switzerland'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_17', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_17'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Switzerland',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_correct_18(self):
        """Sending one of the allowed values as 'iechorNode'
        Purpose:
                Basic test of successful sending of an allowed value for iechorNode
        Sent:
                Allowed value for iechorNode
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_correct_18'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'UK'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_correct_18', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_correct_18'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'UK',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)

    def test_iechorNode_empty_none(self):
        """Sending null/None as 'iechorNode'
        Purpose:
                What happens when we send None
        Sent:
                None
        Expected outcome:
                Error informing that this field cannot be null/None
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_empty_none'
        sent_resource['iechorInfo'] = {
            'iechorNode': None
        }

        expected_response = {
            'iechorInfo': {
                'iechorNode': [
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

        response = self.client.get('/agent/test_iechorNode_empty_none')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorNode_empty_zero_length(self):
        """Sending string of zero length as 'iechorNode'
        Purpose:
                What happens when we send empty string (zero length)
        Sent:
                ''
        Expected outcome:
                Error informing that this field cannot be blank
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_empty_zero_length'
        sent_resource['iechorInfo'] = {
            'iechorNode': ''
        }

        expected_response = {
            'iechorInfo': {
                'iechorNode': [
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

        response = self.client.get('/agent/test_iechorNode_empty_zero_length')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorNode_invalid(self):
        """Sending incorrect value as 'iechorNode'
        Purpose:
                Sending incorrect value as iechorNode
        Sent:
                incorrect value for iechorNode
        Expected outcome:
                Error stating incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_invalid'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'random string here'
        }

        expected_response = {
            'iechorInfo': {
                'iechorNode': [
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

        response = self.client.get('/agent/test_iechorNode_invalid')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorNode_array(self):
        """Sending array as 'iechorNode'
        Purpose:
                What happens when we send wrong type as the field (this case - array of strings and arrays)
        Sent:
                Array with mixed types (strings and arrays)
        Expected outcome:
                Error informing about incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_array'
        sent_resource['iechorInfo'] = {
            'iechorNode': ['a', 'b', 'c', ['d']]
        }

        expected_response = {
            'iechorInfo': {
                'iechorNode': [
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

        response = self.client.get('/agent/test_iechorNode_array')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorNode_dict(self):
        """Sending dictionary as 'iechorNode'
        Purpose:
                What happens when we send wrong type as the field (this case - dict of mixed types)
        Sent:
                Dictionary with mixed types (strings and arrays)
        Expected outcome:
                Error informing about incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_dict'
        sent_resource['iechorInfo'] = {
            'iechorNode': {'a': 'b', 'c': [1, 2, 3]}
        }

        expected_response = {
            'iechorInfo': {
                'iechorNode': [
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

        response = self.client.get('/agent/test_iechorNode_dict')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorNode_number(self):
        """Sending number as 'iechorNode'
        Purpose:
                What happens when we send wrong type as the field (this case - number)
        Sent:
                Number
        Expected outcome:
                Error informing about incorrect value
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_number'
        sent_resource['iechorInfo'] = {
            'iechorNode': 1234567890
        }

        expected_response = {
            'iechorInfo': {
                'iechorNode': [
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

        response = self.client.get('/agent/test_iechorNode_number')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content), expected_response)

    def test_iechorNode_case_sensitive(self):
        """Sending correct value but with wrong case as 'iechorNode'
        Purpose:
                What happens when we send correct value but with incorrect case (denmark instead of Denmark)
        Sent:
                Value with correct string but lowercase (denmark instead of Denmark)
        Expected outcome:
                Resource registered with correct case
        """
        sent_resource = emptyInputAgent()
        sent_resource['id'] = 'test_iechorNode_case_sensitive'
        sent_resource['iechorInfo'] = {
            'iechorNode': 'denmark'
        }

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            '/agent/test_iechorNode_case_sensitive', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['id'] = 'test_iechorNode_case_sensitive'
        expected_resource['iechorInfo'] = {
            'iechorNode': 'Denmark',
            'iechorStatus': None
        }

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertEqual(expected_resource, received_resource)
