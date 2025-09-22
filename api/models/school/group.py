from django.db import models

from ..subject.subject import Subject
from ..with_uuid import WithUUID

from .klass import Klass

class Group(WithUUID):
  order = models.SmallIntegerField('Номер группы')
  klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='groups', verbose_name='Класс')
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='groups', verbose_name='Предмет')
  teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, related_name='groups', verbose_name='Учитель')
  
  lessons: models.Manager
  students: models.Manager
  
  def __str__(self):
    return f'{self.order} по {self.subject} в {self.klass}'
  
  @property
  def allowed_to_edit(self):
    return self.klass.allowed_to_edit
  
  class Meta:
    ordering = ['klass', 'subject', 'order']
    verbose_name = 'Группа'
    verbose_name_plural = 'Группы'