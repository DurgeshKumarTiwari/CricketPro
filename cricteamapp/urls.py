from django.urls import path

from . import views


app_name = 'cricteam'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PointList.as_view(), name='index'),
    path('teams/', views.TeamList.as_view(), name='teams_index'),
    path('teams/<uuid:team_id>/', views.TeamDetails.as_view(), name='teams_detail'),
    path('players/', views.PlayerList.as_view(), name='players_index'),
    path('players/<uuid:player_id>/', views.PlayerDetails.as_view(),
         name='players_detail'),
    path('matches/', views.MatchesCreate.as_view(), name='matches_create'),
    path('matches/fixtures/', views.MatchesFixturesCreate.as_view(),
         name='fixtures_create'),
    path('matches/<uuid:match_id>/', views.MatchesDetail.as_view(),
         name='matches_detail')
]
