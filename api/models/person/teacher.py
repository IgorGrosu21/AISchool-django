from django.db import models

from .person import Person
from ..subject import SubjectName

class Teacher(Person):
  subject_names = models.ManyToManyField(SubjectName, related_name='all_teachers', verbose_name='Предметы')
  experience = models.SmallIntegerField('Стаж работы', default=0)
  
  class Meta:
    verbose_name = 'Учитель'
    verbose_name_plural = 'Учителя'