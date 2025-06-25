from django.urls import path
from api import views

lesson_urlpatterns = [
  path('specific-lessons-preview/<uuid:school>/<uuid:klass>/<str:date_range>/', views.SpecificLessonNamesView.as_view(), name='specific-lessons-names'),
  path('specific-lesson/<uuid:school>/<uuid:klass>/<uuid:lesson>/<str:date>/', views.DetailedSpecificLessonView.as_view(), name='specific-lesson-details'),
  path('specific-lesson-photos/<uuid:school>/<uuid:klass>/<uuid:lesson>/<str:date>/', views.SpecificLessonPhotosView.as_view(), name='specific-lesson-photos'),
  path('specific-lesson-photos/<uuid:school>/<uuid:klass>/<uuid:lesson>/<str:date>/<uuid:pk>/', views.SpecificLessonPhotosView.as_view(), name='specific-lesson-photos'),
  path('homework/<uuid:school>/<uuid:klass>/<uuid:lesson>/<str:date>/', views.DetailedHomeworkView.as_view(), name='homework-details'),
  path('homework-photos/<uuid:school>/<uuid:klass>/<uuid:lesson>/<str:date>/', views.HomeworkPhotosView.as_view(), name='homework-photos'),
  path('homework-photos/<uuid:school>/<uuid:klass>/<uuid:lesson>/<str:date>/<uuid:pk>/', views.HomeworkPhotosView.as_view(), name='homework-photos'),
]