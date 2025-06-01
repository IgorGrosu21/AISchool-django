from django.utils.functional import cached_property
from django.db import models
from uuid import uuid4

from ...person import Balance

class PriceableManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().annotate(
      normalized_cost=models.F('cost') * models.Case(
        models.When(currency='S', then=models.Value(1)),
        models.When(currency='R', then=models.Value(5)),
        models.When(currency='E', then=models.Value(10)),
        models.When(currency='D', then=models.Value(50)),
        default=models.Value(1),
        output_field=models.IntegerField()
      )
    )

class Priceable(models.Model):
  CURRENCIES = {
    'S': 'Sapphire',
    'R': 'Ruby',
    'E': 'Emerald',
    'D': 'Diamond'
  }
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  currency = models.CharField('Валюта', default='S', choices=CURRENCIES, max_length=1)
  cost = models.SmallIntegerField('Цена', default=1)
  objects = PriceableManager()
  
  @cached_property
  def normalized_cost(self):
    return self.cost * Balance.MAPPING[self.get_currency_display().lower()]
  
  class Meta:
    abstract = True