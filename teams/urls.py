from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_team, name='register_team'),

    path('views', views.teams_view, name='teams'),

]
