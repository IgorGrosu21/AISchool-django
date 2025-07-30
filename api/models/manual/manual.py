from django.db import models
from uuid import uuid4

from ..subject import Subject

class Manual(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Название', related_name='manuals')
  grade = models.SmallIntegerField('Класс', default=5)
  slug = models.SlugField('Слаг', max_length=64, unique=True, db_index=True)
  
  modules: models.Manager
  
  def __str__(self):
    return f'{self.grade} {self.subject}'
  
  @property
  def tasks_count(self):
    return sum(module.tasks_count for module in self.modules.all())
  
  class Meta:
    ordering = ['grade', 'subject']
    verbose_name = 'Предмет'
    verbose_name_plural = 'Предметы'