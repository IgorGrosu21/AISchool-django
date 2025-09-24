from django.db import models

from .balance import Balance
from .module import Module
from .with_slug import WithSlug

class Topic(WithSlug):
  module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, verbose_name='Модуль', related_name='topics')

  tasks: models.Manager
  theories: models.Manager

  @property
  def tasks_count(self):
    return self.tasks.count()

  @property
  def balance(self):
    mapping = {currency[0].upper(): currency for currency in Balance.MAPPING.keys()}
    balance = {}
    for task in self.tasks.all():
      key = mapping[task.currency]
      balance.setdefault(key, 0)
      balance[key] += task.cost

    return Balance(**balance)

  class Meta:
    ordering = ['order']
    verbose_name = 'Тема'
    verbose_name_plural = 'Темы'