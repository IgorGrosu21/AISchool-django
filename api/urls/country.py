from django.urls import path
from api.views import country as views

country_urlpatterns = [
  path('city-names/<str:country_slug>/<str:region_slug>/', views.CityNamesView.as_view(), name='city-names'),
  path('region-names/<str:country_slug>/', views.RegionNamesView.as_view(), name='region-names'),
  path('country-names/', views.CountryNamesView.as_view(), name='country-names'),
  path('city/', views.DetailedCityView.as_view(), name='city-details')
]