from datetime import timedelta
from django.utils import timezone
from django.db.models import Q

from api.models import Teacher, Homework, Note

def teacher_with_data(teacher: Teacher):
  lesson_ids = list(teacher.lessons.values_list('id', flat=True))

  teacher.latest_homeworks = list(
    Homework.objects
    .select_related('specific_lesson__lesson__subject', 'student')
    .filter(specific_lesson__lesson_id__in=lesson_ids)
    .order_by('-last_modified')[:4]
  )



  school = teacher.schools.select_related().prefetch_related(
    'timetable',
    'klasses__lessons__teacher'
  ).first()

  if not school:
    teacher.tomorrow_timetable = []
  else:
    tomorrow = timezone.now().date() + timedelta(days=1)
    tomorrow_weekday = tomorrow.strftime('%A')[:2].upper()

    lesson_times = school.timetable.filter(weekday=tomorrow_weekday).order_by('order')
    teacher_lessons_by_time = {}

    for lesson in teacher.lessons.select_related('subject', 'klass').filter(lesson_time__in=lesson_times):
      time_id = lesson.lesson_time.id
      if time_id not in teacher_lessons_by_time:
        teacher_lessons_by_time[time_id] = []
      teacher_lessons_by_time[time_id].append(lesson)

    teacher.tomorrow_timetable = [{
      'id': lesson_time.id,
      'starting': lesson_time.starting,
      'ending': lesson_time.ending,
      'weekday': lesson_time.weekday,
      'order': lesson_time.order,
      'school': school.slug,
      'lessons': teacher_lessons_by_time.get(lesson_time.id, [])
    } for lesson_time in lesson_times]



  work_places = teacher.work_places.select_related('school').prefetch_related(
    'subjects',
    'school__klasses__lessons__teacher'
  ).all()

  all_notes = Note.objects.select_related(
    'specific_lesson__lesson__klass',
    'specific_lesson__lesson__subject'
  ).filter(
    specific_lesson__lesson__teacher=teacher
  ).values('specific_lesson__lesson__klass', 'specific_lesson__lesson__subject', 'value')

  notes_by_klass_subject = {}
  for note in all_notes:
    klass_id = note['specific_lesson__lesson__klass']
    subject_id = note['specific_lesson__lesson__subject']
    key = (klass_id, subject_id)
    if key not in notes_by_klass_subject:
      notes_by_klass_subject[key] = []
    notes_by_klass_subject[key].append(note['value'])

  teacher.analytics = []
  for work_place in work_places:
    klasses = work_place.school.klasses.filter(
      Q(lessons__teacher=teacher) | Q(teacher=teacher)
    ).distinct().order_by('grade')

    school_data = {
      'school': work_place.school,
      'subjects': [{
        'subject_name': subject,
        'klasses': [{
          'slug': klass.slug,
          'values': notes_by_klass_subject.get((klass.id, subject.id), [])
        } for klass in klasses]
      } for subject in work_place.subjects.all()]
    }

    teacher.analytics.append(school_data)

  return teacher