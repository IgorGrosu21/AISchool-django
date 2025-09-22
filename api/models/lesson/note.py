from django.db import models

from ..person.student import Student
from ..with_uuid import WithUUID

from .specific_lesson import SpecificLesson

class Note(WithUUID):
  VALUES = {
    'ma': 'Уважительный пропуск',
    'ua': 'Неуважительный пропуск',
    'da': 'Пропуск по болезни',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    'VG': 'VG',
    'G': 'G',
    'S': 'S',
    'N': 'N'
  }
  value = models.CharField('Значение', choices=VALUES, max_length=2)
  specific_lesson = models.ForeignKey(SpecificLesson, on_delete=models.CASCADE, related_name='notes', verbose_name='Конкретный урок')
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notes', verbose_name='Ученик')
  comment = models.CharField('Комментарий', max_length=256, blank=True, default='')
  last_modified = models.DateTimeField('Время', auto_now=True)
  
  def __str__(self):
    return f'{self.value} для {self.student} по {self.specific_lesson}'
  
  @property
  def allowed_to_edit(self):
    return {self.specific_lesson.lesson.teacher.user.id}, True
  
  @property
  def homework(self):
    homework_qs: 'models.QuerySet' = self.specific_lesson.homeworks.filter(student=self.student)
    if homework_qs.exists():
      return homework_qs.first()
    return None
  
  class Meta:
    verbose_name = 'Оценка'
    verbose_name_plural = 'Оценки'