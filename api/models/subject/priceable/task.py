from django.db import models

from .priceable import Priceable

class Task(Priceable):
  topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True, default=None, verbose_name='Тема', related_name='tasks')
  
  class Meta:
    ordering = ['order']
    verbose_name = 'Задание'
    verbose_name_plural = 'Задания'