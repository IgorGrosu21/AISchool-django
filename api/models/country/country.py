from django.db import models
from uuid import uuid4

class Country(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  name = models.CharField('Название', max_length=32)
  langs = models.CharField('Языки', blank=True, max_length=16)
  flag = models.ImageField('Флаг', blank=True, upload_to='countries/')
  start_grade = models.SmallIntegerField('Младший класс', default=1)
  final_grade = models.SmallIntegerField('Старший класс', default=12)
  school_types = models.CharField('Типы школ', blank=True, max_length=16)
  school_profiles = models.CharField('Профили школ', blank=True, max_length=32)
  
  def __str__(self):
    return f'{self.name}'
  
  class Meta:
    verbose_name = 'Страна'
    verbose_name_plural = 'Страны'
    
#https://www.britannica.com/topic/list-of-countries-1993160