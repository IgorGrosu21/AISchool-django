from django.db import models

from .topic import Topic
from .with_slug import WithSlug

class Theory(WithSlug):
  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, verbose_name='Тема', related_name='theories')
  
  class Meta:
    ordering = ['order']
    verbose_name = 'Теория'
    verbose_name_plural = 'Теории'