from datetime import timedelta
from django.utils import timezone

from api.models import Student

def student_with_data(student: Student):
  lesson_ids = list(student.lessons.values_list('id', flat=True))

  student.tomorrow_timetable = []
  tomorrow = timezone.now().date() + timedelta(days=1)
  tomorrow_weekday = tomorrow.strftime('%A')[:2].upper()

  school = student.klass.school
  student.tomorrow_timetable = []
  lesson_times = school.timetable.none()
  tomorrow = timezone.now().date()
  while not lesson_times.count():
    tomorrow += timedelta(days=1)
    tomorrow_weekday = tomorrow.strftime('%A')[:2].upper()

    lesson_times = school.timetable.filter(weekday=tomorrow_weekday).order_by('order')
  student_lessons_by_time = {}

  for lesson in student.lessons.select_related('subject', 'klass').prefetch_related('specific_lessons').filter(lesson_time__in=lesson_times):
    time_id = lesson.lesson_time.id
    student_lessons_by_time[time_id] = lesson

  for lesson_time in lesson_times:
    lesson = student_lessons_by_time.get(lesson_time.id, None)
    specific_lesson = None
    if lesson:
      specific_lesson = lesson.specific_lessons.filter(date=tomorrow).first()
    student.tomorrow_timetable.append({
      'id': lesson_time.id,
      'starting': lesson_time.starting,
      'ending': lesson_time.ending,
      'weekday': lesson_time.weekday,
      'order': lesson_time.order,
      'school': school.slug,
      'lesson': lesson,
      'specific_lesson': specific_lesson
    })



  student.latest_notes = list(
    student.notes
    .select_related('specific_lesson__lesson__subject')
    .order_by('-last_modified')[:4]
  )



  notes_for_analytics = student.notes.select_related(
    'specific_lesson__lesson__subject'
  ).order_by('specific_lesson__date')

  student.analytics = {}
  for note in notes_for_analytics:
    subject = note.specific_lesson.lesson.subject
    student.analytics.setdefault(subject, []).append({
      'date': note.specific_lesson.date,
      'value': note.value
    })

  student.analytics = [{
    'subject': subject,
    'points': points
  } for subject, points in student.analytics.items()]

  return student