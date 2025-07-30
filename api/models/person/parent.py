from django.db import models

from .person import Person
from .student import Student

class Parent(Person):
  students = models.ManyToManyField(Student, verbose_name='дети', related_name='parents')
  
  @property
  def lessons(self):
    lessons: models.Manager = None
    for student in self.students.all():
      if lessons is None:
        lessons = student.lessons.all()
        continue
      lessons |= student.lessons.all()
    return lessons.distinct()
  
  @property
  def klass_link(self):
    student: Student = self.students.first()
    return f'schools/{student.klass.school.id}/klasses/{student.klass.id}'
  
  @property
  def school_link(self):
    student: Student = self.students.first()
    return f'schools/{student.klass.school.id}'
  
  class Meta:
    verbose_name = 'Родитель'
    verbose_name_plural = 'Родители'