from django.urls import path
from api import views

school_urlpatterns = [
  path('school-names/', views.SchoolNamesView.as_view(), name='school-names'),
  path('school-names/<uuid:city_pk>/', views.SchoolNamesView.as_view(), name='city-school-names'),
  path('schools/', views.SchoolListView.as_view(), name='schools-list'),
  path('schools/<uuid:pk>/', views.DetailedSchoolView.as_view(), name='school-details'),
  path('school-photos/<uuid:school_pk>/', views.SchoolPhotoView.as_view(), name='school-photos'),
  path('school-photos/<uuid:school_pk>/<uuid:pk>/', views.SchoolPhotoView.as_view(), name='school-photos'),
  path('schools/<uuid:pk>/klasses/', views.SchoolKlassesView.as_view(), name='klasses-list'),
  path('schools/<uuid:school_pk>/klasses/<uuid:pk>/', views.DetailedKlassView.as_view(), name='klass-details'),
  path('schools/<uuid:school_pk>/klasses/<uuid:pk>/diary/', views.KlassWithDiaryView.as_view(), name='klass-diary'),
  path('schools/<uuid:pk>/timetable/', views.SchoolTimetableView.as_view(), name='school-timetable'),
]