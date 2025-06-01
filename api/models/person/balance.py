from django.db import models
from uuid import uuid4

class Balance(models.Model):
  MAPPING = { 'sapphires': 1, 'rubies': 5, 'emeralds': 10, 'diamonds': 50 }
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  sapphires = models.SmallIntegerField('Сапфиры', default=0)
  rubies = models.SmallIntegerField('Рубины', default=0)
  emeralds = models.SmallIntegerField('Изумруды', default=0)
  diamonds = models.SmallIntegerField('Бриллианты', default=0)
  networth = models.SmallIntegerField('Состояние', default=0)
  
  def __str__(self):
    return f'{self.student}'
  
  def add_stones(self, num, stone_type):
    setattr(self, stone_type, models.F(stone_type) + num)
    self.networth = models.F('networth') + num * Balance.MAPPING[stone_type]
    self.save(update_fields=[stone_type, 'networth'])
    return self
  
  def add_sapphires(self, num):
    return self.add_stones(num, 'sapphires')
  
  def add_rubies(self, num):
    return self.add_stones(num, 'rubies')
  
  def add_emeralds(self, num):
    return self.add_stones(num, 'emeralds')
  
  def add_diamonds(self, num):
    return self.add_stones(num, 'diamonds')
  
  class Meta:
    verbose_name = 'Баланс'
    verbose_name_plural = 'Балансы'