from django.db import models

from ..media import Media
from .homework import Homework

class HomeworkPhoto(Media):
  file = models.FileField('Файл', upload_to='homeworks/')
  homework = models.ForeignKey(Homework, on_delete=models.CASCADE, verbose_name='Домашнее задание', related_name='files')
  
  class Meta:
    verbose_name = 'Фотография домашнего задания'
    verbose_name_plural = 'Фотографии домашних заданий'