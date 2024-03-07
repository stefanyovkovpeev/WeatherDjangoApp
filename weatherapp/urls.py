from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('randomcities/', views.randomcities, name='randomcities'),
    path('searchedcity', views.search_city, name='searchedcity'),
    path('comparelast10/', views.comparelast10, name='comparelast10'),
    path('refresh/', views.refresh_data, name='refresh_data'),
]
