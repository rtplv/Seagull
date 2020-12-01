from urllib.request import Request

from django.shortcuts import render

# Create your views here.
from gui.services.supervisor import SvService


def index(request: Request):
    process_groups = {}

    for process in SvService().get_all_process_info():
        group_name = process.get('group')

        if group_name in process_groups:
            process_groups[group_name].append(process)
        else:
            process_groups[group_name] = [process]

    print(process_groups)

    return render(request, 'index.html', {
        'process_groups': process_groups
    })
