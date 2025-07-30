from django.urls import path
from api.views import school as views

school_urlpatterns = [
  path('school-names/', views.SchoolNamesView.as_view(), name='school-names'),
  path('schools/', views.SchoolListView.as_view(), name='school-list'),
  path('schools/<uuid:pk>/', views.DetailedSchoolView.as_view(), name='school-details'),
  path('school-photos/<uuid:school_pk>/', views.SchoolPhotoView.as_view(), name='school-photos'),
  path('schools/<uuid:pk>/klasses/', views.SchoolKlassesView.as_view(), name='school-klasses'),
  path('schools/<uuid:pk>/timetable/', views.SchoolTimetableView.as_view(), name='school-timetable'),
  path('klasses/<uuid:school_pk>/<uuid:pk>/', views.DetailedKlassView.as_view(), name='klass-details'),
]