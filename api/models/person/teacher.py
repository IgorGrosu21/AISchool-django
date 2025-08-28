from django.db import models
from django.db.models import Q

from .person import Person
from ..subject import Subject

SELF_DEVELOPMENT_LINK = 'selfdev'

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
      return f'schools/{self.klass.school.slug}/klasses/{self.klass.slug}'
  
  @property
  def school_link(self):
    if self.schools.exists():
      return f'schools/{self.schools.first().slug}'
  
  @property
  def diary_link(self):
    schools = self.schools
    if schools.count() == 1:
      return f'diary/teachers/{self.id}/{schools.first().slug}'
    return f'diary/teachers/{self.id}'
  
  @property
  def journal_link(self):
    schools = self.schools
    if schools.count() == 1:
      if hasattr(self, 'klass'):
        return f'journal/teachers/{self.id}/{schools.first().slug}/{self.klass.slug}/{SELF_DEVELOPMENT_LINK}'
      return f'journal/teachers/{self.id}/{schools.first().slug}'
    return f'journal/teachers/{self.id}'
  
  class Meta:
    verbose_name = 'Учитель'
    verbose_name_plural = 'Учителя'