import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

class Command(BaseCommand):
    help = 'Sends enrollment reminder emails to students'

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days',type=int)
    
    def handle(self, *args, **options):
        emails = []
        subject = 'Enroll in course'
        date_joined = datetime.date.today() - datetime.timedelta(days=options['days'])
        users = User.objects.annotate(course_count=Count('course_joined')).filter(course_count=0, date_joined__lte=date_joined)
        for user in users:
            message = f'Hello {user.username}, please enroll in a course'
            emails.append((subject, message, settings.DEFAULT_FROM_EMAIL, [user.email]))
        send_mass_mail(emails)
        self.stdout.write(f'Sent {len(emails)} reminders')