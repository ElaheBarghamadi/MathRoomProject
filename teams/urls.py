from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_view, name='teams'),

    # path('', views.register_team, name='register_team'),
]
