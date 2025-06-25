from django.db import models
from uuid import uuid4

from ..user import User

class Person(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='%(class)s_account', verbose_name='Пользователь')
  
  def __str__(self):
    return f'{self.user}'
  
  class Meta:
    abstract = True