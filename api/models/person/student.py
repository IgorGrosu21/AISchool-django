from django.db import models

from .person import Person
from .subscription import Subscription
from ..subject.balance import Balance
from ..school import Klass
from ..subject import Subject, Module, Topic, Theory, Task

class Student(Person):
  klass = models.ForeignKey(Klass, on_delete=models.SET_NULL, null=True, related_name='students', verbose_name='Класс', blank=True)
  subscription = models.OneToOneField(Subscription, on_delete=models.SET_NULL, null=True, related_name='student', verbose_name='Подписка', blank=True)
  balance = models.OneToOneField(Balance, on_delete=models.SET_NULL, related_name='student', verbose_name='Баланс', null=True, blank=True)
  is_manager = models.BooleanField('Является менеджером', default=False)
  completed_theories = models.ManyToManyField(Theory, verbose_name='Выполненные теории', blank=True)
  completed_tasks = models.ManyToManyField(Task, verbose_name='Выполненные задания', blank=True)
  
  def subject_priceables(self, priceable: models.Manager, subject: Subject):
    return priceable.filter(topic__module__subject=subject).count()
  
  def module_priceables(self, priceable: models.Manager, module: Module):
    return priceable.filter(topic__module=module).count()
  
  def topic_priceables(self, priceable: models.Manager, topic: Topic):
    return priceable.filter(topic=topic).count()
  
  def calc_progress(self, with_priceables: Subject | Module | Topic):
    priceables_gatherer = None
    if isinstance(with_priceables, Subject):
      priceables_gatherer = self.subject_priceables
    elif isinstance(with_priceables, Module):
      priceables_gatherer = self.module_priceables
    elif isinstance(with_priceables, Topic):
      priceables_gatherer = self.topic_priceables
    if priceables_gatherer:
      priceables_count = priceables_gatherer(self.completed_theories, with_priceables) + priceables_gatherer(self.completed_tasks, with_priceables)
    else:
      priceables_count = 0
    if with_priceables.priceables_count == 0:
      return 0
    return round(priceables_count / with_priceables.priceables_count, 2)
  
  def get_priceables(self, name: str):
    return self.completed_theories if name == 'theories' else self.completed_tasks
  
  def add_priceable(self, priceable: Theory | Task):
    if isinstance(priceable, Theory):
      self.completed_theories.add(priceable)
    else:
      self.completed_tasks.add(priceable)
    self.balance.add_stones(priceable.cost, priceable.get_currency_display())
  
  def delete(self):
    self.balance.delete()
    self.subscription.delete()
    super().delete()
    
  @property
  def rank(self):
    if self.klass:
      return self.klass.students.filter(balance__networth__gt=self.balance.networth).count() + 1
    return 1
  
  class Meta:
    verbose_name = 'Ученик'
    verbose_name_plural = 'Ученики'