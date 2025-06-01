from django.db import models
from uuid import uuid4

from .user import User

class Social(models.Model):
  TYPES = (
    ('ig', 'Instagram'),
    ('fb', 'Facebook'),
  )
  
  id = models.UUIDField(primary_key=True, default=uuid4)
  type = models.CharField('Соц. сеть', max_length=2, choices=TYPES)
  link = models.URLField('Ссылка')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='socials', verbose_name='Пользователь')
  
  class Meta:
    verbose_name = 'Ссылка на соц. сеть'
    verbose_name_plural = 'Ссылки на соц. сети'
  
  def __str__(self):
    return self.link