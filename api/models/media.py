from urllib.parse import urljoin

from django.db import models

from core.settings import HOST

from .with_uuid import WithUUID

class Media(WithUUID):
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

class WithFiles(WithUUID):
  files: 'models.QuerySet[Media]'

  class Meta:
    abstract = True