from django.db import models

from .priceable import Priceable

class Theory(Priceable):
  topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True, default=None, verbose_name='Тема', related_name='theories')
  
  class Meta:
    ordering = ['order']
    verbose_name = 'Теория'
    verbose_name_plural = 'Теории'