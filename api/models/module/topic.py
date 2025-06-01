from django.utils.functional import cached_property
from django.db import models
from uuid import uuid4

from .module import Module

class TopicManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().annotate(cost=
      models.Sum('tasks__normalized_cost') + models.Sum('theories__normalized_cost') 
    )

class Topic(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, default=None, verbose_name='Модуль', related_name='topics')
  name = models.CharField('Название', max_length=256)
  objects = TopicManager
  
  def __str__(self):
    return f'{self.name} в {self.module}'
  
  @cached_property
  def cost(self):
    return sum(self.tasks.values_list('cost', flat=True)) + sum(self.theories.values_list('cost', flat=True))
  
  class Meta:
    verbose_name = 'Тема'
    verbose_name_plural = 'Темы'