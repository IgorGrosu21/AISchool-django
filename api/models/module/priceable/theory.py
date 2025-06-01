from django.db import models

from .priceable import Priceable

class Theory(Priceable):
  topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True, default=None, verbose_name='Тема', related_name='theories')
  name = models.CharField('Название', max_length=128)
  slug = models.SlugField('Слаг', max_length=128)
  
  def __str__(self):
    return f'{self.name} в {self.topic}'
  
  class Meta:
    verbose_name = 'Теория'
    verbose_name_plural = 'Теории'