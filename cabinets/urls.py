from django.urls import path

from . import views

app_name = 'cabinets'

urlpatterns = [
    path('', views.index, name='index'),
    path('cabinetttttytytytyttyytytytyttt/<int:cabinet_id>/', views.detail, name='detail'),
    path('newcabinet/', views.new_cabinet, name='new_cabinet'),
    path('dashboard/', views.covid_dashboard, name='covid_dashboard'),
    path('privacy/', views.privacy_policy, name='privacy_policy')
]