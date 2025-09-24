from django.db import models

from ..person.teacher import Teacher
from ..subject.subject import Subject
from ..with_uuid import WithUUID

from .school import School

class Klass(WithUUID):
  PROFILES = {
    'R': 'Реальный',
    'U': 'Гуманитарный',
  }
  grade = models.SmallIntegerField('Цифра', default=1)
  letter = models.CharField('Буква', default='A', max_length=1)
  teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, verbose_name='Классный руководитель', related_name='klass', blank=True)
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='klasses', verbose_name='Школа')
  subjects = models.ManyToManyField(Subject, through='Lesson', verbose_name='Уроки')
  profile = models.CharField('Профиль', choices=PROFILES, default='R', max_length=1)
  slug = models.SlugField('Слаг', max_length=3, db_index=True)

  lessons: models.Manager
  students: models.Manager
  groups: models.Manager

  @property
  def networth(self) -> int:
    return sum(student.balance.networth for student in self.students.exclude(balance=None))

  @property
  def allowed_to_edit(self):
    school_allowed_to_edit, _ = self.school.allowed_to_edit
    return school_allowed_to_edit | ({self.teacher.user.id} if self.teacher else set()), True

  def __str__(self):
    return f'{self.grade}{self.letter} {self.school}'

  class Meta:
    ordering = ['school', 'grade', 'letter']
    verbose_name = 'Класс'
    verbose_name_plural = 'Классы'