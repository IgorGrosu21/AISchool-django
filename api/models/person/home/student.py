class StudentHome:
  @property
  def latest_notes(self):
    return self.notes.order_by('-last_modified')[:4]

  @property
  def latest_specific_lessons(self):
    SpecificLesson = self.lessons.model.specific_lessons.model

    lesson_ids = self.lessons.values_list('id', flat=True)
    return SpecificLesson.objects.filter(lesson_id__in=lesson_ids).order_by('-last_modified')[:4]

  @property
  def analytics(self):
    return [{
      'subject': subject,
      'points': [{
        'date': note.specific_lesson.date,
        'value': note.value
      } for note in self.notes.filter(specific_lesson__lesson__subject=subject).order_by('specific_lesson__date')]
    } for subject in self.klass.subjects.distinct()]