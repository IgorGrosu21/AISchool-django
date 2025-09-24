from django.db import models

from ..subject.subject import Subject

from .person import Person

from .routes.teacher import TeacherRoutes

class Teacher(Person, TeacherRoutes):
  subjects = models.ManyToManyField(Subject, related_name='all_teachers', verbose_name='Предметы')
  experience = models.SmallIntegerField('Стаж работы', default=0)

  schools: models.Manager
  lessons: models.Manager
  groups: models.Manager
  work_places: models.Manager

  @property
  def is_manager(self) -> bool:
    return self.work_places.filter(is_manager=True).exists()

  class Meta:
    verbose_name = 'Учитель'
    verbose_name_plural = 'Учителя'