from datetime import timedelta
from django.utils import timezone
from django.db.models import Q

from ...lesson.note import Note
from ...lesson.homework import Homework

class TeacherHome:
  @property
  def latest_homeworks(self):
    lesson_ids = self.lessons.values_list('id', flat=True)
    return Homework.objects.filter(specific_lesson__lesson_id__in=lesson_ids).order_by('-last_modified')[:4]
  
  @property
  def tomorrow_timetable(self):
    school = self.schools.first()
    if not school:
      return []
    tomorrow = timezone.now().date() + timedelta(days=1)
    tomorrow_weekday = tomorrow.strftime('%A')[:2].upper()
    return [{
      'id': lesson_time.id,
      'starting': lesson_time.starting,
      'ending': lesson_time.ending,
      'weekday': lesson_time.weekday,
      'order': lesson_time.order,
      'school': school.slug,
      'lessons': self.lessons.filter(lesson_time=lesson_time)
    } for lesson_time in school.timetable.filter(weekday=tomorrow_weekday).order_by('order')]
  
  @property
  def analytics(self):
    get_notes = lambda klass, subject: Note.objects.filter(
      specific_lesson__lesson__klass=klass,
      specific_lesson__lesson__subject=subject
    ).values_list('value', flat=True)
    return [{
      'school': work_place.school,
      'subjects': [{
        'subject_name': subject,
        'klasses': [{
          'slug': klass.slug,
          'values': get_notes(klass, subject)
        } for klass in work_place.school.klasses.filter(Q(lessons__teacher=self) | Q(teacher=self)).distinct().order_by('grade')]
      } for subject in work_place.subjects.all()]
    } for work_place in self.work_places.all()]