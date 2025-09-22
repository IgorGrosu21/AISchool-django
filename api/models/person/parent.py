from django.db import models

from .person import Person
from .student import Student

from .routes.parent import ParentRoutes

class Parent(Person, ParentRoutes):
  students = models.ManyToManyField(Student, verbose_name='дети', related_name='parents')
  
  class Meta:
    verbose_name = 'Родитель'
    verbose_name_plural = 'Родители'