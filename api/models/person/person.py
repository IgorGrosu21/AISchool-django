from django.db import models

from ..with_uuid import WithUUID

class Person(WithUUID):
  user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='%(class)s_account', verbose_name='Пользователь')
  
  klass_link: str | None
  school_link: str | None
  diary_link: str | None
  journal_link: str | None
  
  @property
  def allowed_to_edit(self):
    return self.user.allowed_to_edit
  
  @property
  def profile_type(self) -> str | None:
    return self.user.account_type
  
  def __str__(self):
    return f'{self.user}'
  
  class Meta:
    abstract = True