from django.db import models
from uuid import uuid4

from ..user import User
from .subscription import Subscription
from .balance import Balance
from ..school import Klass

class Student(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', verbose_name='Пользователь')
  klass = models.ForeignKey(Klass, on_delete=models.SET_NULL, null=True, default=None, related_name='students', verbose_name='Класс')
  subscription = models.OneToOneField(Subscription, on_delete=models.CASCADE, null=True, default=None, related_name='user', verbose_name='Подписка', blank=True)
  balance = models.OneToOneField(Balance, on_delete=models.CASCADE, related_name='student', verbose_name='Баланс', null=True, blank=True)
  is_manager = models.BooleanField('Является менеджером', default=False)
  
  def __str__(self):
    return f'{self.user}'
  
  def delete(self):
    self.balance.delete()
    super().delete()
    
  @property
  def rank(self):
    if self.klass:
      return self.klass.students.filter(balance__networth__gt=self.balance.networth).count() + 1
    return 1
  
  class Meta:
    verbose_name = 'Ученик'
    verbose_name_plural = 'Ученики'