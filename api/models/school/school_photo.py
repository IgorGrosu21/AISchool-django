from django.db import models

from ..media import Media
from .school import School

class SchoolPhoto(Media):
  is_preview = models.BooleanField('Является превью', default=False)
  file = models.ImageField('Файл', upload_to='schools/')
  school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа', related_name='files')
  
  class Meta:
    ordering = ['-is_preview']
    verbose_name = 'Фотография школы'
    verbose_name_plural = 'Фотографии школ'