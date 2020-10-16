from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:squirrel_id>/', views.detail, name='detail'),
        path('add/', views.add, name='add'),
        path('create/', views.create, name='create'),
        path('map/', views.map, name='map'),
        path('<int:squirrel_id>/edit/', views.edit, name='edit'),
        ]
