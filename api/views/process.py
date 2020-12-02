from urllib.request import Request
from django.http import JsonResponse
from api.services.supervisor import SvService


def start(request: Request):
    return JsonResponse({
        'success': SvService().start_process()
    })


def stop(request: Request):
    return JsonResponse({
        'success': SvService().stop_process()
    })
