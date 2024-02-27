from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create a superuser with specified role or group'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--role', type=str, help='Specify the role for the superuser')

    def handle(self, *args, **options):
        role_name = options['role']
        username = options['username']
        email = options['email']
        password = options['password']

        # Create superuser
        super().handle(*args, **options)

        # Add superuser to specified group
        if role_name:
            try:
                group = Group.objects.get(name=role_name)
                user = self.UserModel.objects.get(username=username)
                user.groups.add(group)
                self.stdout.write(self.style.SUCCESS(f'Superuser {username} added to group {role_name} successfully.'))
            except Group.DoesNotExist:
                self.stderr.write(self.style.ERROR(f'Group {role_name} does not exist.'))
