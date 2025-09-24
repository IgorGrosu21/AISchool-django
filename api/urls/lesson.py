from django.urls import path
from api.views import lesson as views

BY_SCHOOL = '<str:school_slug>'
BY_ACCOUNT = '<str:account_type>/<uuid:person_pk>'
BY_KLASS = f'{BY_SCHOOL}/<str:klass_slug>'
BY_LESSON = f'{BY_KLASS}/<uuid:lesson_pk>'
BY_DATE_RANGE = '<str:date_range>'

lesson_urlpatterns = [
  path(f'lesson-names/{BY_ACCOUNT}/', views.LessonNamesView.as_view(), name='lesson-names'),
  path(f'specific-lessons-names/{BY_ACCOUNT}/{BY_DATE_RANGE}/', views.SpecificLessonNamesView.as_view(), name='specific-lesson-names'),
  path(f'specific-lessons/{BY_LESSON}/<str:date>/', views.DetailedSpecificLessonView.as_view(), name='specific-lesson-details'),
  path(f'specific-lesson-photos/{BY_LESSON}/<str:date>/', views.SpecificLessonPhotosView.as_view(), name='specific-lesson-photos'),
  path(f'homeworks/{BY_LESSON}/<uuid:specific_lesson_pk>/<uuid:student_pk>/', views.DetailedHomeworkView.as_view(), name='homework-details'),
  path(f'homework-photos/{BY_LESSON}/<uuid:specific_lesson_pk>/<uuid:student_pk>/', views.HomeworkPhotosView.as_view(), name='homework-photos'),
  path(f'student-notes/<uuid:student_pk>/{BY_DATE_RANGE}/', views.StudentNoteListView.as_view(), name='student-notes-list'),
  path(f'teacher-notes/<uuid:teacher_pk>/{BY_KLASS}/<str:subject_slug>/{BY_DATE_RANGE}/', views.TeacherNoteListView.as_view(), name='teacher-notes-list'),
  path(f'notes/{BY_LESSON}/<uuid:student_pk>/', views.NoteCreateView.as_view(), name='notes-create'),
]