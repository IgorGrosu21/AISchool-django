from django.db import models

from ..manual.balance import Balance
from ..manual.manual import Manual
from ..manual.module import Module
from ..manual.task import Task
from ..manual.topic import Topic
from ..school.group import Group
from ..school.klass import Klass

from .person import Person
from .subscription import Subscription

from .routes.student import StudentRoutes

class Student(Person, StudentRoutes):
  klass = models.ForeignKey(Klass, on_delete=models.SET_NULL, null=True, related_name='students', verbose_name='Класс', blank=True)
  subscription = models.OneToOneField(Subscription, on_delete=models.SET_NULL, null=True, related_name='student', verbose_name='Подписка', blank=True)
  balance = models.OneToOneField(Balance, on_delete=models.SET_NULL, related_name='student', verbose_name='Баланс', null=True, blank=True)
  groups = models.ManyToManyField(Group, verbose_name='Группы', related_name='students')
  is_manager = models.BooleanField('Является менеджером', default=False)
  completed_tasks = models.ManyToManyField(Task, verbose_name='Выполненные задания', blank=True)

  homeworks: models.Manager
  notes: models.Manager
  parents: models.Manager

  @property
  def lessons(self):
    lessons = self.klass.lessons.all()
    for group in self.groups.all().prefetch_related('lessons'):
      lessons |= group.lessons.all()
    return lessons.distinct()

  @property
  def rank(self):
    if self.klass:
      return self.klass.students.filter(balance__networth__gt=self.balance.networth).count() + 1
    return 1

  def calc_progress(self, with_tasks: Manual | Module | Topic) -> float:
    mapping = {
      Manual: 'topic__module__subject',
      Module: 'topic__module',
      Topic: 'topic',
    }
    filter_key = mapping.get(type(with_tasks))

    if not filter_key or not with_tasks.tasks_count:
      return 0

    tasks_count = self.completed_tasks.filter(**{filter_key: with_tasks}).count()
    return round(tasks_count / with_tasks.tasks_count, 2)

  def add_task_to_completed(self, task: Task):
    self.completed_tasks.add(task)
    self.balance.add_stones(task.cost, task.get_currency_display())

  def delete(self):
    if self.balance:
      self.balance.delete()
    if self.subscription:
      self.subscription.delete()
    super().delete()

  class Meta:
    verbose_name = 'Ученик'
    verbose_name_plural = 'Ученики'