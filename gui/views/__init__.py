from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from api.services.supervisor import SvService


@ensure_csrf_cookie
def index(request: HttpRequest) -> HttpResponse:
    sv_service = SvService()

    return render(request, 'index.html', {
        'sv': {
            'version': sv_service.get_version(),
            'state': sv_service.get_state()
        }
    })