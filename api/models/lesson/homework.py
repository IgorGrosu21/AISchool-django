from django.db import models

from ..media import WithFiles
from ..person.student import Student

from .specific_lesson import SpecificLesson

class Homework(WithFiles):
  specific_lesson = models.ForeignKey(SpecificLesson, on_delete=models.CASCADE, related_name='homeworks', verbose_name='Конкретный урок')
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='homeworks', verbose_name='Ученик')
  comment = models.CharField('Комментарий', max_length=256, blank=True)
  last_modified = models.DateTimeField('Время', auto_now=True)
  links = models.TextField('Ссылки', blank=True)
  
  @property
  def allowed_to_edit(self):
    return {self.student.user.id}, True
  
  def __str__(self):
    return f'{self.student} на {self.specific_lesson}'
  
  @property
  def note(self):
    note_qs: 'models.QuerySet' = self.specific_lesson.notes.filter(student=self.student)
    if note_qs.exists():
      return note_qs.first()
    return None
  
  class Meta:
    verbose_name = 'Домашнее задание'
    verbose_name_plural = 'Домашние задания'