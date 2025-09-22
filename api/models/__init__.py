from .country.city import City
from .country.country import Country
from .country.region import Region

class CountryModels:
  City = City
  Country = Country
  Region = Region

from .lesson.homework import Homework
from .lesson.homework_photo import HomeworkPhoto
from .lesson.lesson import Lesson
from .lesson.lesson_time import LessonTime
from .lesson.note import Note
from .lesson.specific_lesson import SpecificLesson
from .lesson.specific_lesson_photo import SpecificLessonPhoto

class LessonModels:
  Homework = Homework
  HomeworkPhoto = HomeworkPhoto
  Lesson = Lesson
  LessonTime = LessonTime
  Note = Note
  SpecificLesson = SpecificLesson
  SpecificLessonPhoto = SpecificLessonPhoto

from .manual.balance import Balance
from .manual.manual import Manual
from .manual.module import Module
from .manual.task import Task
from .manual.theory import Theory
from .manual.topic import Topic

class ManualModels:
  Balance = Balance
  Manual = Manual
  Module = Module
  Task = Task
  Theory = Theory
  Topic = Topic


from .person.parent import Parent
from .person.person import Person
from .person.student import Student
from .person.subscription import Subscription
from .person.teacher import Teacher

class PersonModels:
  Parent = Parent
  Person = Person
  Student = Student
  Subscription = Subscription
  Teacher = Teacher


from .school.group import Group
from .school.klass import Klass
from .school.position import Position
from .school.school import School
from .school.school_photo import SchoolPhoto

class SchoolModels:
  Group = Group
  Klass = Klass
  Position = Position
  School = School
  SchoolPhoto = SchoolPhoto


from .subject.subject import Subject
from .subject.subject_type import SubjectType

class SubjectModels:
  Subject = Subject
  SubjectType = SubjectType


from .user.social import Social
from .user.user import User

class UserModels:
  Social = Social
  User = User


from .media import Media, WithFiles