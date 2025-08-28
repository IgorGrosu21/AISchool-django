from django.db import models
from uuid import uuid4
from urllib.parse import urljoin
from core.settings import HOST

class Media(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  file: models.FileField
  
  @staticmethod
  def append_prefix(path):
    if not HOST:
      raise ValueError("HOST setting is required for media URL generation")
    return urljoin(HOST, f'media/{path}')
  
  def get_absolute_url(self):
    return self.append_prefix(self.file)
  
  def __str__(self):
    return self.file.name
  
  class Meta:
    abstract = True
    
class WithFiles(models.Model):
  files: 'models.QuerySet[Media]'
  
  class Meta:
    abstract = True