from api import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('process/all/', views.process.get_all_processes, name='get_all_processes'),
    path('process/start/', views.process.start, name='process-start'),
    path('process/restart/', views.process.restart, name='process-restart'),
    path('process/stop/', views.process.stop, name='process-stop')
]