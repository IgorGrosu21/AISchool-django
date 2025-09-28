from django.db import models

from ..with_uuid import WithUUID

class WithSlug(WithUUID):
  name = models.CharField('Название', max_length=192)
  slug = models.SlugField('Слаг', max_length=128, db_index=True)
  order = models.SmallIntegerField('Порядок', default=0)

  def __str__(self):
    return self.name

  class Meta:
    abstract = True

class Paginated(WithSlug):
  start_page = models.SmallIntegerField('Начальная страница')
  end_page = models.SmallIntegerField('Конечная страница')

  class Meta:
    abstract = True