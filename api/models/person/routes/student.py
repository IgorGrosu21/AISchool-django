from ...school.klass import Klass

class StudentRoutes:
  klass: Klass

  @property
  def school(self):
    return self.klass.school if self.klass else None

  @property
  def klass_link(self):
    if self.klass:
      return f'schools/{self.klass.school.slug}/klasses/{self.klass.slug}'

  @property
  def school_link(self):
    if self.school:
      return f'schools/{self.school.slug}'

  @property
  def diary_link(self):
    if self.klass:
      return f'diary/students/{self.id}/{self.klass.school.slug}'

  @property
  def journal_link(self):
    if self.klass:
      return f'journal/students/{self.id}'