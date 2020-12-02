from urllib.request import Request
from django.shortcuts import render

from api.services.supervisor import SvService


def index(request: Request):
    process_groups = {}
    sv_service = SvService()

    for process in sv_service.get_all_process_info():
        group_name = process.get('group')

        if group_name in process_groups:
            process_groups[group_name].append(process)
        else:
            process_groups[group_name] = [process]

    print(sv_service.get_state())

    return render(request, 'index.html', {
        'sv': {
            'version': sv_service.get_version(),
            'state': sv_service.get_state()
        },
        'process_groups': process_groups
    })
