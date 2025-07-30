from functools import wraps

from auth.models import AuthUser
from api.models import Person

class UserRoutes:
  account: AuthUser
  account_type: str
  person: Person
  
  def handle_staff(func):
    @wraps(func)
    def wrapped(self: 'UserRoutes'):
      if self.account.is_staff:
        return None
      return func(self)
    return wrapped
  
  @property
  @handle_staff
  def profile_link(self):
    return f'{self.account_type}s/{self.person.id}'
  
  @property
  @handle_staff
  def klass_link(self) -> str | None:
    return self.person.klass_link
  
  @property
  @handle_staff
  def school_link(self) -> str | None:
    return self.person.school_link