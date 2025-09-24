from api.models import Student, SpecificLesson

def student_with_data(student: Student):
  lesson_ids = list(student.lessons.values_list('id', flat=True))

  student.latest_notes = list(
    student.notes
    .select_related('specific_lesson__lesson__subject')
    .order_by('-last_modified')[:4]
  )



  student.latest_specific_lessons = list(
    SpecificLesson.objects
    .select_related('lesson__subject')
    .filter(lesson_id__in=lesson_ids)
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