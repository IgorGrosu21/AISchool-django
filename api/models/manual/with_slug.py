from django.db import models
from uuid import uuid4

class WithSlug(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  name = models.CharField('Название', max_length=192)
  slug = models.SlugField('Слаг', max_length=64, db_index=True)
  order = models.SmallIntegerField('Порядок', default=0)
  
  def __str__(self):
    return self.name
  
  class Meta:
    abstract = True