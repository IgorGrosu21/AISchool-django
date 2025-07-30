from django.urls import path
from api.views import lesson as views

lesson_urlpatterns = [
  path('lesson-time-names/<uuid:school_pk>/', views.LessonTimeNamesView.as_view(), name='lesson-time-names'),
  path('lesson-names/<str:account_type>/<uuid:person_pk>/', views.LessonNamesView.as_view(), name='lesson-names'),
  path('specific-lessons-names/<str:account_type>/<uuid:person_pk>/<str:date_range>/', views.SpecificLessonNamesView.as_view(), name='specific-lesson-names'),
  path('specific-lessons/<uuid:school>/<uuid:klass>/<uuid:lesson>/<str:date>/', views.DetailedSpecificLessonView.as_view(), name='specific-lesson-details'),
  path('specific-lesson-photos/<uuid:school>/<uuid:klass>/<uuid:lesson>/<str:date>/', views.SpecificLessonPhotosView.as_view(), name='specific-lesson-photos'),
  path('homeworks/<uuid:school>/<uuid:klass>/<uuid:lesson>/<uuid:specific_lesson>/<uuid:student>/', views.DetailedHomeworkView.as_view(), name='homework-details'),
  path('homework-photos/<uuid:school>/<uuid:klass>/<uuid:lesson>/<uuid:specific_lesson>/<uuid:student>/', views.HomeworkPhotosView.as_view(), name='homework-photos')
]