# -*- coding: UTF-8 -*-
from rest_framework import status
from iechor.test_baseobject import BaseTestObject
from iechor.test_datastructure_json import emptyInputAgent, emptyOutputAgent
import json


class TestResource(BaseTestObject):

    def test_resource_creation_correct(self):
        """Sending one of allowed values as 'accessibility'
        Purpose:
                Basic test of successful sending of an allowed value for accessibility
        Sent:
                Allowed value for accessibility
        Expected outcome:
                Resource registered with the sent value
        """
        sent_resource = emptyInputAgent()
        sent_resource['accessibility'] = ['Open access']

        response = self.client.post('/agent/', sent_resource, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/agent/Resource_Name', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_resource = emptyOutputAgent()

        expected_resource['bioagentsID'] = 'Resource_Name'
        expected_resource['accessibility'] = ['Open access']

        received_resource = json.loads(response.content)
        received_resource['additionDate'] = None
        received_resource['lastUpdate'] = None

        self.assertItemsEqual(expected_resource, received_resource)
