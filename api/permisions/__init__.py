from .lesson import CanEditHomework, CanEditSpecificLesson
from .person import (
  IsSelf, IsSelfOrReadonly,
  IsParent, IsParentOrReadonly,
  IsStudent, IsStudentOrReadonly,
  IsKlassManager, IsKlassManagerOrReadonly,
  IsTeacher, IsTeacherOrReadonly,
  IsSchoolManager, IsSchoolManagerOrReadonly,
)
from .school import CanEditSchool, CanEditKlass
from .user import CanCreateUser