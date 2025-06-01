from django.utils.functional import cached_property
from django.db import models
from uuid import uuid4

from .school import School
from ..subject import SubjectName

class KlassManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().annotate(networth=models.Sum('students__balance__networth'))

class Klass(models.Model):
  PROFILES = {
    'R': 'Реальный',
    'U': 'Гуманитарный',
  }
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  grade = models.SmallIntegerField('Цифра', default=1)
  letter = models.CharField('Буква', default='A', max_length=1)
  teacher = models.OneToOneField('Teacher', on_delete=models.SET_NULL, null=True, verbose_name='Классный руководитель', blank=True)
  school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, default=None, related_name='klasses', verbose_name='Школа')
  lessons = models.ManyToManyField(SubjectName, through='Lesson', verbose_name='Уроки')
  profile = models.CharField('Профиль', choices=PROFILES, default='R', max_length=1)
  
  def __str__(self):
    return f'{self.grade}{self.letter} {self.school}'
  
  @cached_property
  def networth(self):
    return sum(self.students.values_list('balance__networth', flat=True))
  
  @property
  def allowed_to_edit(self):
    return self.school.allowed_to_edit + [self.teacher.user.id]
  
  class Meta:
    verbose_name = 'Класс'
    verbose_name_plural = 'Классы'