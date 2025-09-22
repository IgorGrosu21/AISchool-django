from django.db import models

from .balance import Balance
from .module import Module
from .with_slug import WithSlug

class Topic(WithSlug):
  module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, verbose_name='Модуль', related_name='topics')
  
  tasks: models.Manager
  theories: models.Manager
  
  def __str__(self):
    return self.name
  
  def cost(self, currency):
    return sum(self.tasks.filter(currency=currency).values_list('cost', flat=True))
  
  @property
  def tasks_count(self):
    return self.tasks.count()
  
  @property
  def balance(self):
    return Balance(**{currency: self.cost(currency[0].upper()) for currency in Balance.MAPPING.keys()})
  
  class Meta:
    ordering = ['order']
    verbose_name = 'Тема'
    verbose_name_plural = 'Темы'