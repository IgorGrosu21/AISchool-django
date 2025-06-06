from django.urls import path
from api import views

country_urlpatterns = [
  path('city-names/<uuid:region_pk>/', views.CityNamesView.as_view(), name='city-names'),
  path('region-names/<uuid:country_pk>/', views.RegionNamesView.as_view(), name='region-names'),
  path('country-names/', views.CountryNamesView.as_view(), name='country-names'),
  path('city/', views.CityView.as_view(), name='city-details')
]