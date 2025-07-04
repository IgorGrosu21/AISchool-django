from django.utils.functional import cached_property
from django.db import models
from uuid import uuid4

from .school import School
from ..subject import SubjectName

class Klass(models.Model):
  PROFILES = {
    'R': 'Реальный',
    'U': 'Гуманитарный',
  }
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  grade = models.SmallIntegerField('Цифра', default=1)
  letter = models.CharField('Буква', default='A', max_length=1)
  teacher = models.OneToOneField('Teacher', on_delete=models.SET_NULL, null=True, verbose_name='Классный руководитель', related_name='klass', blank=True)
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='klasses', verbose_name='Школа')
  lessons = models.ManyToManyField(SubjectName, through='Lesson', related_name='lessons', verbose_name='Уроки')
  profile = models.CharField('Профиль', choices=PROFILES, default='R', max_length=1)
  
  def __str__(self):
    return f'{self.grade}{self.letter} {self.school}'
  
  @property
  def networth(self):
    return sum(student.balance.networth for student in self.students.exclude(balance=None))
  
  @property
  def allowed_to_edit(self):
    school_allowed_to_edit, _ = self.school.allowed_to_edit
    return school_allowed_to_edit | ({self.teacher.user.id} if self.teacher else set()), True
  
  class Meta:
    ordering = ['school', 'grade', 'letter']
    verbose_name = 'Класс'
    verbose_name_plural = 'Классы'