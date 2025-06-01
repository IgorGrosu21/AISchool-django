from django.db import models

from .priceable import Priceable

class Task(Priceable):
  topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True, default=None, verbose_name='Тема', related_name='tasks')
  name = models.CharField('Название', max_length=64)
  slug = models.SlugField('Слаг', max_length=64)
  
  def __str__(self):
    return f'{self.name} в {self.topic}'
  
  class Meta:
    verbose_name = 'Задание'
    verbose_name_plural = 'Задания'