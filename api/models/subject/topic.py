from django.db import models
from uuid import uuid4

from .balance import Balance
from .module import Module

class Topic(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, default=None, verbose_name='Модуль', related_name='topics')
  name = models.CharField('Название', max_length=256)
  slug = models.SlugField('Слаг', max_length=64, db_index=True)
  order = models.SmallIntegerField('Порядок', default=0)
  
  def __str__(self):
    return self.name
  
  def cost(self, priceables, currency):
    return sum(priceables.filter(currency=currency).values_list('cost', flat=True))
  
  def priceables_cost(self, currency):
    return self.cost(self.theories.all(), currency) + self.cost(self.tasks.all(), currency)
  
  @property
  def priceables_count(self):
    return self.theories.count() + self.tasks.count()
  
  @property
  def balance(self):
    return Balance(**{currency: self.priceables_cost(currency[0].upper()) for currency in Balance.MAPPING.keys()})
  
  class Meta:
    ordering = ['order']
    verbose_name = 'Тема'
    verbose_name_plural = 'Темы'