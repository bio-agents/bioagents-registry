from rest_framework import serializers
from iechor.models import *
from iechor.validators import *

class AgentTypeSerializer(serializers.ModelSerializer):
	name = serializers.CharField(allow_blank=False, validators=[IsStringTypeValidator], required=False)

	class Meta:
		model = AgentType
		fields = ('name',)

	def get_pk_field(self, model_field):
		return None

	def to_representation(self, obj):
		return obj.name

	# need to add validation here since this method overrides all validation
	def to_internal_value(self, data):
		# checking if blank
		IsNotBlankValidator(data)
		# checking if within enum
		enum = ENUMValidator(['Bioinformatics portal','Command-line agent', 'Web application', 'Desktop application', 'Script', 'Suite', 'Workbench', 'Database portal', 'Ontology', 'Workflow', 'Plug-in', 'Library', 'Web API', 'Web service', 'SPARQL endpoint'])
		data = enum(data)
		return {'name': data}