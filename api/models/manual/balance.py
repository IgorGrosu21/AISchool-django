from django.db import models

from ..with_uuid import WithUUID

class Balance(WithUUID):
  MAPPING = { 'sapphires': 1, 'rubies': 5, 'emeralds': 10, 'diamonds': 50 }
  sapphires = models.SmallIntegerField('Сапфиры', default=0)
  rubies = models.SmallIntegerField('Рубины', default=0)
  emeralds = models.SmallIntegerField('Изумруды', default=0)
  diamonds = models.SmallIntegerField('Бриллианты', default=0)
  networth = models.SmallIntegerField('Состояние', default=0)
  
  def __str__(self):
    return f'{self.student}'
  
  def add_stones(self, quantity: int, stone_type: str):
    setattr(self, stone_type, models.F(stone_type) + quantity)
    self.networth = models.F('networth') + quantity * Balance.MAPPING[stone_type]
    self.save(update_fields=[stone_type, 'networth'])
    return self
  
  def __add__(self, other: 'Balance'):
    return Balance(
      sapphires = self.sapphires + other.sapphires,
      rubies = self.rubies + other.rubies,
      emeralds = self.emeralds + other.emeralds,
      diamonds = self.diamonds + other.diamonds
    )
    
  @staticmethod
  def default():
    return Balance(
      sapphires = 0,
      rubies = 0,
      emeralds = 0,
      diamonds = 0
    )
  
  class Meta:
    verbose_name = 'Баланс'
    verbose_name_plural = 'Балансы'