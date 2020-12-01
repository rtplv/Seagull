from django.views import generic

# Create your views here.
from gui.models import ProgramGroup


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'groups'
    model = ProgramGroup


class GroupDetailView(generic.DetailView):
    model = ProgramGroup
    context_object_name = 'group'
    template_name = 'group_detail.html'
