from django.db import models
from uuid import uuid4
from core.settings import HOST

class Media(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  
  @staticmethod
  def append_prefix(path):
    return f'{HOST}/media/{path}'
  
  def get_absolute_url(self):
    return self.append_prefix(self.file.name)
  
  def __str__(self):
    return self.file.name
  
  class Meta:
    abstract = True