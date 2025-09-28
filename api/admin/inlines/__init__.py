from .country import RegionInline, CityInline
from .lesson import HomeworkPhotoInline, HomeworkInline, LessonInline, NoteInline, SpecificLessonInline, SpecificLessonPhotoInline
from .manual import ManualInline, TaskInline, ModuleInline, TopicInline
from .person import StudentInline
from .school import GroupInline, KlassInline, PositionInline, SchoolPhotoInline
from .subject import SubjectInline
from .user import SocialInline

#we also incapsulate our models

from .through import ParentStudentInline, StudentGroupInline, TeacherSubjectInline