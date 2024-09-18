from django.conf import settings
from django.core.management.base import BaseCommand, CommandError, CommandParser
from iechor.models import *
from iechor.serializers import *
from django.core.mail import send_mail
import datetime


def get_resource_info(d: str) -> None:
	try:
		day = datetime.datetime.strptime(d, '%Y-%m-%d').date()
		print('Running task for date:', day)
		send_updates(day)
	except (ValueError, TypeError) as _:
		print('No (valid) date provided, defaulting to yesterday...')
		yesterday = datetime.date.today() - datetime.timedelta(days=1)
		send_updates(yesterday)

def format_agent_results(res):
	return [
		(
			settings.URL_FRONT + r.bioagentsID,
			r.bioagentsID,
			r.name,
			str(r.additionDate),
			str(r.lastUpdate),
			str(r.owner)
		)
		for r in res
	]


def get_new_agents(day: datetime.date):
	res = Resource.objects.filter(visibility=1, additionDate__date=day).order_by('bioagentsID')
	return format_agent_results(res)
	
def get_updated_agents(day: datetime.date):
	res = Resource.objects.filter(visibility=1, lastUpdate__date=day).order_by('bioagentsID')
	return format_agent_results(res)

def get_deleted_agents(day: datetime.date):
	res = Resource.objects.filter(visibility=0, lastUpdate__date=day).order_by('bioagentsID')
	l = []
	for r in res:
		# if the resource has visibility = 0 and there are no other instances of it with visibility = 1
		if len(Resource.objects.filter(visibility=1, bioagentsID=r.bioagentsID)) == 0:
			l.append(r)
	return format_agent_results(l)


def agents_to_string(t):
	return '\t'.join(t)

def send_updates(day: datetime.date) -> None:

	
	subject = f'Agent updates on: {day}'
	agents_header_text = 'link\tbioagentsID\tname\tadditionDate\tlastUpdate\tuser\n'
	
	message = 'Summary of agent operations\n'
	message += '\n\nNew agents:\n'
	message += agents_header_text
	new = get_new_agents(day)
	for t in new:
		message += agents_to_string(t) + '\n'


	message += '\n\nUpdated agents:\n'
	message += agents_header_text
	updated = get_updated_agents(day)
	for t in updated:
		message += agents_to_string(t) + '\n'
	
	
	message += '\n\nDeleted agents:\n'
	message += agents_header_text
	deleted = get_deleted_agents(day)
	for t in deleted:
		message += agents_to_string(t) + '\n'
	
	print(message)
	if settings.ADMIN_EMAIL_LIST:
		print('Sending email to admins')
		send_mail(
			subject=subject,
			message=message,
			from_email=settings.DEFAULT_FROM_EMAIL,
			recipient_list=settings.ADMIN_EMAIL_LIST
		)
	else:
		print('No admins configured to send emails, only printed to console.')
	
	

class Command(BaseCommand):
	help = 'Sending updates to admin'
	
	
	def add_arguments(self, parser: CommandParser) -> None:
		parser.add_argument('-d', '--date', type=str, help='Provide a custom date', )

	def handle(self, *args, **options):
		self.stdout.write('Sending updates to admins...')
		get_resource_info(options['date'])
		self.stdout.write('Done.')