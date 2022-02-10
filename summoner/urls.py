from django.urls import include, path
from django.contrib import admin
from summoner import views
from summoner.views import SummonerView, DetailView, RenewView, InGameView

app_name = 'summoner'

urlpatterns = [
    path('', views.index, name='index'),  # sorae.gg/
    path('summoner/', SummonerView.as_view(), name='search'),  # sorae.gg/summoner/?userName=
    path('detail/', DetailView.as_view()), # sorae.gg/detail/?matchID=
    path('renew/', RenewView.as_view()), # sorae.gg/renew/?userName=
    path('ingame/', InGameView.as_view()), # sorae.gg/ingame/?userName=
]
