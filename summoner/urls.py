from django.urls import include, path
from django.contrib import admin
from summoner import views
from summoner.views import SummonerView, MainView, DetailView

app_name = 'summoner'

urlpatterns = [
    path('', views.index, name='index'),  # sorae.gg/
    path('summoner/', SummonerView.as_view(), name='search'),  # sorae.gg/summoner/?userName=
    path('validation/', MainView.as_view()), # sorae.gg/api/
    path('detail/', DetailView.as_view()), # sorae.gg/detail/
]
