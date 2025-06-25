from django.db import models
from uuid import uuid4

from .balance import Balance
from .subject import Subject

class Module(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, default=None, verbose_name='Предмет', related_name='modules')
  name = models.CharField('Название', max_length=256)
  slug = models.SlugField('Слаг', max_length=64, db_index=True)
  order = models.SmallIntegerField('Порядок', default=0)
  
  def __str__(self):
    return self.name
  
  @property
  def priceables_count(self):
    return sum(topic.priceables_count for topic in self.topics.all())
  
  @property
  def balance(self):
    return sum([topic.balance for topic in self.topics.all()], Balance.default())
  
  class Meta:
    ordering = ['order']
    verbose_name = 'Модуль'
    verbose_name_plural = 'Модули'