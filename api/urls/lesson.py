from django.urls import path
from api.views import lesson as views

by_school = '<str:school_slug>'
by_account = '<str:account_type>/<uuid:person_pk>'
by_klass = f'{by_school}/<str:klass_slug>'
by_lesson = f'{by_klass}/<uuid:lesson_pk>'
by_date_range = '<str:date_range>'

lesson_urlpatterns = [
  path(f'lesson-names/{by_account}/', views.LessonNamesView.as_view(), name='lesson-names'),
  path(f'specific-lessons-names/{by_account}/{by_date_range}/', views.SpecificLessonNamesView.as_view(), name='specific-lesson-names'),
  path(f'specific-lessons/{by_lesson}/<str:date>/', views.DetailedSpecificLessonView.as_view(), name='specific-lesson-details'),
  path(f'specific-lesson-photos/{by_lesson}/<str:date>/', views.SpecificLessonPhotosView.as_view(), name='specific-lesson-photos'),
  path(f'homeworks/{by_lesson}/<uuid:specific_lesson_pk>/<uuid:student_pk>/', views.DetailedHomeworkView.as_view(), name='homework-details'),
  path(f'homework-photos/{by_lesson}/<uuid:specific_lesson_pk>/<uuid:student_pk>/', views.HomeworkPhotosView.as_view(), name='homework-photos'),
  path(f'student-notes/<uuid:student_pk>/{by_date_range}/', views.StudentNoteListView.as_view(), name='student-notes-list'),
  path(f'teacher-notes/<uuid:teacher_pk>/{by_klass}/<str:subject_slug>/{by_date_range}/', views.TeacherNoteListView.as_view(), name='teacher-notes-list'),
  path(f'notes/{by_lesson}/<uuid:student_pk>/', views.NoteCreateView.as_view(), name='notes-create'),
]