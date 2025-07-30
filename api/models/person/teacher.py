from django.db import models

from .person import Person
from ..subject import Subject

class Teacher(Person):
  subjects = models.ManyToManyField(Subject, related_name='all_teachers', verbose_name='Предметы')
  experience = models.SmallIntegerField('Стаж работы', default=0)
  
  schools: models.Manager
  lessons: models.Manager
  groups: models.Manager
  work_places: models.Manager
  
  @property
  def is_manager(self) -> bool:
    return self.work_places.filter(is_manager=True).exists()
  
  @property
  def klass_link(self):
    if hasattr(self, 'klass'):
      return f'schools/{self.klass.school.id}/klasses/{self.klass.id}'
  
  @property
  def school_link(self):
    if self.schools.exists():
      return f'schools/{self.schools.first().id}'
  
  class Meta:
    verbose_name = 'Учитель'
    verbose_name_plural = 'Учителя'