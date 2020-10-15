from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:squirrel_id>/', views.detail, name='detail'),
        path('add/', views.add, name='add'),
        ]
