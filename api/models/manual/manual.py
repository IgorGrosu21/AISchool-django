from django.db import models

from ..subject.subject import Subject
from ..with_uuid import WithUUID

class Manual(WithUUID):
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Название', related_name='manuals')
  grade = models.SmallIntegerField('Класс', default=5)
  slug = models.SlugField('Слаг', max_length=64, unique=True, db_index=True)

  modules: models.Manager

  @property
  def tasks_count(self):
    return sum(module.tasks_count for module in self.modules.all())

  def __str__(self):
    return f'{self.grade} {self.subject}'

  class Meta:
    ordering = ['grade', 'subject']
    verbose_name = 'Учебник'
    verbose_name_plural = 'Учебник'