from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('list', views.WeatherListView.as_view(), name='list'),
    path('add-city', views.AddNewRegionView.as_view(), name='add_city'),
]