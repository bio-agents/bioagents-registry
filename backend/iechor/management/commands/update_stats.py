from django.core.management.base import BaseCommand, CommandError
from iechor.tasks import *
import json, os


class Command(BaseCommand):
	help = 'Update Agent Statistics'

	def handle(self, *args, **options):

		generate_missing_stats()

		self.stdout.write('All done.')
