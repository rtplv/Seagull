from django.urls import path

from gui import views

app_name = 'gui'

urlpatterns = [
    path('', views.index, name='index')
]
