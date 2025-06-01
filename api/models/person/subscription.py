from django.db import models
from uuid import uuid4

class Subscription(models.Model):
  PLANS = {
    'A': 'monthly',
    'Y': 'yearly',
    'K': 'klass',
    'L': 'lifetime'
  }
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  plan = models.CharField('План', default='Y', choices=PLANS, max_length=1)
  price = models.SmallIntegerField('Цена', default=1000)
  ending = models.DateField('Конец')
  
  def __str__(self):
    return f'{self.plan} для {self.user}'
  
  class Meta:
    verbose_name = 'Подписка'
    verbose_name_plural = 'Подписки'