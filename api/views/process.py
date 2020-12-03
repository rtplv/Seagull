import json
from django.http import JsonResponse, HttpRequest, HttpResponse
from api.services.supervisor import SvService


def get_all_processes(request: HttpRequest) -> HttpResponse:
    process_groups = {}
    sv_service = SvService()

    for process in sv_service.get_all_process_info():
        group_name = process.get('group')

        if group_name in process_groups:
            process_groups[group_name].append(process)
        else:
            process_groups[group_name] = [process]

    return JsonResponse({
        'data': process_groups
    })


def start(request: HttpRequest) -> HttpResponse:
    params = json.loads(request.body)

    return JsonResponse({
        'success': SvService().start_process(params.get('name'))
    })


def restart(request: HttpRequest) -> HttpResponse:
    params = json.loads(request.body)

    return JsonResponse({
        'success': SvService().restart_process(params.get('name'))
    })


def stop(request: HttpRequest) -> HttpResponse:
    params = json.loads(request.body)

    return JsonResponse({
        'success': SvService().stop_process(params.get('name'))
    })


def tail_process_stdout(request: HttpRequest) -> HttpResponse:
    params = json.loads(request.body)

    return JsonResponse({
        'data': SvService().tail_process_stdout_log(params.get('name'))
    })


def tail_process_stderr(request: HttpRequest) -> HttpResponse:
    params = json.loads(request.body)

    return JsonResponse({
        'data': SvService().tail_process_stderr_log(params.get('name'))
    })
