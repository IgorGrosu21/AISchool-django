from django.db import models

from ..with_uuid import WithUUID
from .region import Region

class City(WithUUID):
  name = models.CharField('Название', max_length=32)
  region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name='Регион', related_name='cities')
  holidays = models.TextField('Каникулы')

  schools: models.Manager
  user: models.Manager

  def __str__(self):
    return f'{self.region}, {self.name}'

  class Meta:
    ordering = ['region__country', 'region', 'name']
    verbose_name = 'Город'
    verbose_name_plural = 'Города'