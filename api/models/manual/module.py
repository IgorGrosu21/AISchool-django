from django.db import models

from .balance import Balance
from .manual import Manual
from .with_slug import WithSlug

class Module(WithSlug):
  manual = models.ForeignKey(Manual, on_delete=models.SET_NULL, null=True, verbose_name='Предмет', related_name='modules')

  topics: models.Manager

  @property
  def tasks_count(self):
    return sum(topic.tasks_count for topic in self.topics.all())

  @property
  def balance(self):
    return sum([topic.balance for topic in self.topics.all()], Balance.default())

  class Meta:
    ordering = ['order']
    verbose_name = 'Модуль'
    verbose_name_plural = 'Модули'