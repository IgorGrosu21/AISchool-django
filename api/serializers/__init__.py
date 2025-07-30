from .detailed import DetailedCitySerializer
from .detailed import DetailedHomeworkSerializer, DetailedSpecificLessonSerializer
from .detailed import DetailedModuleSerializer, DetailedManualSerializer, DetailedTopicSerializer
from .detailed import DetailedParentSerializer, DetailedStudentSerializer, DetailedTeacherSerializer
from .detailed import DetailedKlassSerializer, DetailedSchoolSerializer, SchoolWithKlassesSerializer, SchoolWithTimetableSerializer
from .detailed import DetailedUserSerializer, UserRoutesSerializer

from .listed import LessonSerializer, HomeworkSerializer, SpecificLessonSerializer
from .listed import ManualSerializer
from .listed import StudentSerializer
from .listed import SchoolSerializer

from .name import CityNameSerializer, RegionNameSerializer, CountryNameSerializer
from .name import LessonTimeNameSerializer, LessonNameSerializer, SpecificLessonNameSerializer, SpecificLessonWithHomeworkSerializer
from .name import ProgressSerializer
from .name import SchoolNameSerializer
from .name import SubjectNameSerializer

from .media import MediaSerializer, DetailedMediaSerializer

#I import only those serializers that are used in api.views