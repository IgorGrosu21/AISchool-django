from django.db import models

SELF_DEVELOPMENT_LINK = 'selfdev'

class TeacherRoutes:
  schools: models.Manager
  
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