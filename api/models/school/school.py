from django.db import models
from uuid import uuid4

from .position import Position
from ..country import City

class School(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  name = models.CharField('Название', max_length=64)
  positions = models.ManyToManyField('Teacher', through=Position, verbose_name='Позиции', related_name='schools')
  city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город', related_name='schools')
  address = models.CharField('Адрес', max_length=64)
  lang = models.CharField('Язык', blank=True, max_length=2)
  type = models.CharField('Тип', max_length=1, blank=True)
  profiles = models.CharField('Профили', max_length=16, blank=True)
  start_grade = models.SmallIntegerField('Младший класс', default=1)
  final_grade = models.SmallIntegerField('Старший класс', default=12)
  desc = models.TextField('Описание', default='', blank=True)
  phones = models.CharField('Телефоны', max_length=64, default='', blank=True)
  emails = models.CharField('Эл. почты', max_length=128, default='', blank=True)
  website = models.URLField('Сайт', default='', blank=True)
  work_hours = models.CharField('Часы работы', max_length=16, blank=True)
  
  @property
  def preview(self):
    return self.photos.filter(is_preview=True).first()
  
  @preview.setter
  def preview(self, file):
    preview_qs = self.photos.filter(is_preview=True)
    if preview_qs.exists():
      preview_qs.update(file=file)
    else:
      self.photos.create(is_preview=True, file=file, school=self)
  
  @property
  def managers(self):
    return self.positions.through.objects.filter(is_manager=True)
  
  @property
  def head_master(self):
    return self.positions.through.objects.filter(type='HM').first()
  
  @property
  def head_teachers(self):
    return self.positions.through.objects.filter(type='HT')
  
  @property
  def allowed_to_edit(self):
    return set(self.managers.values_list('teacher__user__id', flat=True)), True
  
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Школа'
    verbose_name_plural = 'Школы'