from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from iechor.permissions import IsOwnerOrReadOnly, HasEditPermissionToEditResourceOrReadOnly, CanConcludeResourceRequest, IsStaffOrReadOnly
from iechor.models import *
from iechor.serializers import *

class Environment(APIView):
	"""
	Returns the deployment info of the server.
	"""	

	def get(self, request, format=None):
		if settings.DEPLOYMENT == 'dev':
			return Response("Development");
		return Response("Production")