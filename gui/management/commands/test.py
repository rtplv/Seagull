from django.core.management.base import BaseCommand
from gui.models import Program, ProgramGroup


class Command(BaseCommand):
    def handle(self, *args, **options):
        # all = Program.objects.all()

        group = ProgramGroup(name='Indexing')
        group.save()

        print(group)

        # program = Program()
        # program.name = 'markering'
        # program.pid = 52
        # program.group = ocas_group
        # program.save()
        #
        # program = Program()
        # program.name = 'listen_some_queue'
        # program.pid = 2
        # program.group = pirabit_group
        # program.save()

        # sorted_programs = Program.objects.order_by('name')

        # last = Program.objects.filter(id=5).get()
        # p = Program(name='Test', pid=25)
        # p.save()

        # print(sorted_programs)
