from django.urls import path

from gui import views

app_name = 'gui'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('group/<int:pk>', views.GroupDetailView.as_view(), name='group_detail')
]
