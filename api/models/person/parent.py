from django.db import models

from .person import Person
from .student import Student

class Parent(Person):
  students = models.ManyToManyField(Student, verbose_name='дети', related_name='parents')
  
  @property
  def klass_link(self):
    student: Student = self.students.first()
    return f'schools/{student.klass.school.slug}/klasses/{student.klass.slug}'
  
  @property
  def school_link(self):
    student: Student = self.students.first()
    return f'schools/{student.klass.school.slug}'
  
  @property
  def diary_link(self):
    students = self.students
    if students.count() == 1:
      return f'diary/students/{students.first().id}'
    return f'diary/parents/{self.id}'
  
  @property
  def journal_link(self):
    students = self.students
    if students.count() == 1:
      return f'journal/students/{students.first().id}'
    return f'journal/parents/{self.id}'
  
  class Meta:
    verbose_name = 'Родитель'
    verbose_name_plural = 'Родители'