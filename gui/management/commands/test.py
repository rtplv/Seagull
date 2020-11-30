from django.core.management.base import BaseCommand
from gui.models import Program, ProgramGroup


class Command(BaseCommand):
    def handle(self, *args, **options):
        # all = Program.objects.all()

        # profiles_group = ProgramGroup()
        # profiles_group.name = 'Profiles'
        # profiles_group.save()
        #
        # print(profiles_group)
        #
        # program = Program()
        # program.name = 'recount_statistic'
        # program.pid = 2
        # program.group = profiles_group
        # program.save()

        profiles_group = ProgramGroup.objects.get(pk=3)

        profiles_group.program_set.create(name='activity_stat', pid=10)
        profiles_group.program_set.create(name='pass_data', pid=11)

        # last = Program.objects.filter(id=5).get()
        # p = Program(name='Test', pid=25)
        # p.save()

        print(profiles_group)
