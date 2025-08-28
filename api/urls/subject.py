from django.urls import path
from api.views import subject as views

subject_urlpatterns = [
  path('subject-names/', views.SubjectNamesView.as_view(), name='subject-names'),
  path('teached-subjects/<uuid:teacher_pk>/<str:school_slug>/<str:klass_slug>/', views.TeachedSubjectsView.as_view(), name='teached-subjects'),
  path('studied-subjects/<uuid:student_pk>/', views.StudiedSubjectsView.as_view(), name='studied-subjects'),
]