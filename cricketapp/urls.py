from django.urls import path
from . import views


app_name = 'cricket_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('register-team/', views.register_team, name='register-team'),
    path('create_team/', views.create_team, name='create-team'),
    path('add_player/', views.add_players, name='add_player'),
    path('user-register/', views.userRegister, name='user-register'),
    path('user-login/', views.userLogin, name='user-login'),
    path('my-team', views.myTeam, name='my-team'),
    path('create-team', views.createTeam, name='create-team'),
    path('logout', views.userLogout, name='logout'),
    path('team-players/', views.teamPlayers, name='team-players'),
    path('add-player/', views.addPlayer, name='add-player'),
    path('team-matches/', views.teamMatches, name='team-matches'),
    path('upcoming-match/', views.addUpcomingMatch, name='upcoming-match'),
    path('start-match/<str:pk>', views.startMatch, name='start-match'),
    path('add-batsman/<str:pk>', views.addBatsman, name='add-batsman'),
    path('add-1/<str:pk>', views.add1, name='add-1'),
    path('add-recent-match', views.addRecentMatch, name='add-recent-match'),
    path('add-scorecard/<str:pk>', views.addScoreCard, name='add-scorecard'),
]
