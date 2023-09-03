"""
- python manage.py <command>

"""
# 0
# create "./<my-app>/management/commands/<commands>.py" and write bellow code
# also create init files: "/<my-app>/management/__init__.py" & "./<my-app>/management/commands/__init__.py"
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = 'remove all expired otp codes'

	def handle(self, *args, **options):
		# .......
		self.stdout.write('all expired otp codes removed.')
