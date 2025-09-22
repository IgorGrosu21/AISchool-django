from django.db import models

from ..media import Media

from .specific_lesson import SpecificLesson

class SpecificLessonPhoto(Media):
  file = models.FileField('Файл', upload_to='specific_lessons/')
  specific_lesson = models.ForeignKey(SpecificLesson, on_delete=models.CASCADE, verbose_name='Конкретный урок', related_name='files')
  
  class Meta:
    verbose_name = 'Фотография к конкретному уроку'
    verbose_name_plural = 'Фотографии к конкретным урокам'