from django.db import models
from uuid import uuid4

class Priceable(models.Model):
  CURRENCIES = {
    'S': 'sapphires',
    'R': 'rubies',
    'E': 'emeralds',
    'D': 'diamonds'
  }
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  currency = models.CharField('Валюта', default='S', choices=CURRENCIES, max_length=1)
  cost = models.SmallIntegerField('Цена', default=1)
  name = models.CharField('Название', max_length=128)
  slug = models.SlugField('Слаг', max_length=64, db_index=True)
  order = models.SmallIntegerField('Порядок', default=0)
  
  def __str__(self):
    return self.name
  
  class Meta:
    abstract = True