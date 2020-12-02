from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from api.services.supervisor import SvService


def index(request: HttpRequest) -> HttpResponse:
    sv_service = SvService()

    return render(request, 'index.html', {
        'sv': {
            'version': sv_service.get_version(),
            'state': sv_service.get_state()
        }
    })