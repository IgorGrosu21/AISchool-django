from django.db import models

from ..with_uuid import WithUUID

class Country(WithUUID):
  name = models.CharField('Название', max_length=32)
  langs = models.CharField('Языки', blank=True, max_length=16)
  flag = models.ImageField('Флаг', blank=True, upload_to='countries/')
  start_grade = models.SmallIntegerField('Младший класс', default=1)
  final_grade = models.SmallIntegerField('Старший класс', default=12)
  school_types = models.CharField('Типы школ', blank=True, max_length=16)
  school_profiles = models.CharField('Профили школ', blank=True, max_length=32)
  slug = models.SlugField('Слаг', max_length=2, db_index=True, unique=True)

  regions: models.Manager
  subject_types: models.Manager

  def __str__(self):
    return f'{self.name}'

  class Meta:
    verbose_name = 'Страна'
    verbose_name_plural = 'Страны'
    
#https://www.britannica.com/topic/list-of-countries-1993160