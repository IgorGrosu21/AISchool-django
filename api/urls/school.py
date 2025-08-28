from django.urls import path
from api.views import school as views

school_urlpatterns = [
  path('school-names/', views.SchoolNamesView.as_view(), name='school-names'),
  path('schools/', views.SchoolListView.as_view(), name='school-list'),
  path('schools/<str:slug>/', views.DetailedSchoolView.as_view(), name='school-details'),
  path('school-photos/<str:school_slug>/', views.SchoolPhotoView.as_view(), name='school-photos'),
  path('schools/<str:slug>/klasses/', views.SchoolKlassesView.as_view(), name='school-klasses'),
  path('schools/<str:slug>/timetable/', views.SchoolTimetableView.as_view(), name='school-timetable'),
  path('schools/<str:slug>/lesson-times/', views.SchoolLessonTimesView.as_view(), name='school-lesson-times'),
  path('klasses/<str:school_slug>/<str:slug>/', views.DetailedKlassView.as_view(), name='klass-details'),
  path('teacher_klasses/<str:school_slug>/<uuid:teacher_pk>/', views.TeacherKlasses.as_view(), name='teacher-klasses'),
]