from auth.models import AuthUser

from ..person.parent import Parent
from ..person.person import Person
from ..person.student import Student
from ..person.teacher import Teacher

class UserLogic:
  account: AuthUser
  
  @property
  def is_account_verified(self) -> bool:
    return self.account.is_verified
  
  @property
  def parent(self) -> Parent | None:
    return self.parent_account if hasattr(self, 'parent_account') else None
  
  @property
  def student(self) -> Student | None:
    return self.student_account if hasattr(self, 'student_account') else None
  
  @property
  def teacher(self) -> Teacher | None:
    return self.teacher_account if hasattr(self, 'teacher_account') else None
  
  @property
  def is_parent(self):
    return self.parent != None
  
  @property
  def is_teacher(self):
    return self.teacher != None
  
  @property
  def is_student(self):
    return self.student != None
  
  @property
  def account_type(self) -> str | None:
    if self.is_teacher:
      return 'teacher'
    elif self.is_parent:
      return 'parent'
    elif self.is_student:
      return 'student'
    elif self.account.is_staff:
      return 'staff'
    return None
  
  @property
  def person(self) -> Person | None:
    if self.is_teacher:
      return self.teacher
    elif self.is_parent:
      return self.parent
    elif self.is_student:
      return self.student
    return None