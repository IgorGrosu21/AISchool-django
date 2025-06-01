from django.utils.functional import cached_property
from django.db import models
from uuid import uuid4

from ..subject import Subject

class Module(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, default=None, verbose_name='Предмет', related_name='modules')
  name = models.CharField('Название', max_length=256)
  
  def __str__(self):
    return f'{self.name} по {self.subject}'
  
  @cached_property
  def cost(self):
    return sum(self.topics.values_list('cost', flat=True))
  
  class Meta:
    verbose_name = 'Модуль'
    verbose_name_plural = 'Модули'