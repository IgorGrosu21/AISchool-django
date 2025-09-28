from django.db import models

from .topic import Topic
from .utils import WithSlug

class Task(WithSlug):
  CURRENCIES = { 'S': 'sapphires', 'R': 'rubies', 'E': 'emeralds', 'D': 'diamonds' }

  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, verbose_name='Тема', related_name='tasks')
  currency = models.CharField('Валюта', default='S', choices=CURRENCIES, max_length=1)
  cost = models.SmallIntegerField('Цена', default=1)

  class Meta:
    ordering = ['order']
    verbose_name = 'Задание'
    verbose_name_plural = 'Задания'