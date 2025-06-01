from django.db import models
from uuid import uuid4

from ..person import Student
from .module import Module
from .priceable import Theory, Task

class ModuleProgress(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='modules_progress', verbose_name='Ученик')
  module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='student_progress', verbose_name='Модуль')
  completed_theories = models.ManyToManyField(Theory, verbose_name='Выполненные теории', blank=True)
  completed_tasks = models.ManyToManyField(Task, verbose_name='Выполненные задания', blank=True)
  percent = models.CharField('Процент выполнения', max_length=3, default='0')
  
  def __str__(self):
    return f'{self.student} выполнил {self.module} на {self.percent}%'
  
  def complete_theory(self, theory):
    self.completed_theories.add(theory)
    self.percent = str(round(sum(self.completed_theories.values_list('normalized_cost', flat=True)) / self.module.cost))
    self.save()
  
  def complete_task(self, task):
    self.completed_tasks.add(task)
    self.percent = str(round(sum(self.completed_tasks.values_list('normalized_cost', flat=True)) / self.module.cost))
    self.save()
  
  class Meta:
    verbose_name = 'Прогресс модуля'
    verbose_name_plural = 'Прогрессы модулей'