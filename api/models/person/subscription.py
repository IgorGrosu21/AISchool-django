from django.db import models

from ..with_uuid import WithUUID

class Subscription(WithUUID):
  PLANS = {
    'A': 'monthly',
    'Y': 'yearly',
    'K': 'klass',
    'L': 'lifetime'
  }
  plan = models.CharField('План', default='Y', choices=PLANS, max_length=1)
  price = models.SmallIntegerField('Цена', default=1000)
  ending = models.DateField('Конец')
  
  def __str__(self):
    return f'{self.plan} для {self.student}'
  
  class Meta:
    verbose_name = 'Подписка'
    verbose_name_plural = 'Подписки'