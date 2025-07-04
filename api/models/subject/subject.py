from django.db import models
from uuid import uuid4

from .subject_name import SubjectName

class Subject(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  name = models.ForeignKey(SubjectName, on_delete=models.CASCADE, verbose_name='Название', related_name='subjects')
  grade = models.SmallIntegerField('Класс', default=5)
  slug = models.SlugField('Слаг', max_length=64, unique=True, db_index=True)
  
  def __str__(self):
    return f'{self.grade} {self.name}'
  
  @property
  def priceables_count(self):
    return sum(module.priceables_count for module in self.modules.all())
  
  class Meta:
    ordering = ['grade', 'name']
    verbose_name = 'Предмет'
    verbose_name_plural = 'Предметы'