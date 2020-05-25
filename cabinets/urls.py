from django.urls import path

from . import views

app_name = 'cabinets'

urlpatterns = [
    # ex: /cabinet/
    path('', views.index, name='index'),
    # ex: /cabinet/5/
    path('<int:cabinet_id>/', views.detail, name='detail'),
    # ex: /cabinet/5/results/
    path('newcabinet/', views.new_cabinet, name='new_cabinet'),
    # ex: /cabinet/5/update/
    #path('<int:cabinet_id>/update/', views.update, name='update')
]