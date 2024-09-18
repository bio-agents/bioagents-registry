import json, random, datetime, time, re, uuid
import iechor.search as search
import iechor.iechor_logging as iechor_logging
import iechor.stats as stats
from rest_framework import status, generics
from django.utils.decorators import method_decorator
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from iechor.models import Resource, Function, Domain
from django.http import Http404
from iechor.serializers import *
from iechor.permissions import IsOwnerOrReadOnly, HasEditPermissionToEditResourceOrReadOnly, CanConcludeResourceRequest, IsStaffOrReadOnly
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, renderer_classes, permission_classes, authentication_classes, parser_classes
from rest_framework.renderers import JSONRenderer
from django.conf import settings
from elasticsearch import Elasticsearch
from collections import Counter
from django.db.models import Count
from iechorapp import settings
from django.db.models import Q
from pprint import pprint

from iechor.view.resource import *
from iechor.view.domain import *
from iechor.view.stats import *
from iechor.view.workflow import *
from iechor.view.issues import *
from iechor.view.user import *
from iechor.view.environment import *
from iechor.view.agents import *
from iechor.view.edam import *


def issue_function(resource, user):
	# check for issues
	pass
	# EDAMTopicIssue([resource], user=user).report()
	# EDAMOperationIssue([resource], user=user).report()
	# EDAMDataIssue([resource], user=user).report()
	# EDAMFormatIssue([resource], user=user).report()
	# NoLicenseIssue([resource], user=user).report()
	# NoContactIssue([resource], user=user).report()
	# NoTOSIssue([resource], user=user).report()
