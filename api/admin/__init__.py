from .country import CountryAdmin, RegionAdmin, CityAdmin
from .lesson import HomeworkAdmin, LessonTimeAdmin, LessonAdmin, NoteAdmin, SpecificLessonAdmin
from .manual import BalanceAdmin, ManualAdmin, ModuleAdmin, TaskAdmin, TheoryAdmin, TopicAdmin
from .person import ParentAdmin, StudentAdmin, SubscriptionAdmin, TeacherAdmin
from .school import GroupAdmin, KlassAdmin, PositionAdmin, SchoolAdmin
from .user import SocialAdmin, UserAdmin
from .subject import SubjectAdmin, SubjectTypeAdmin

#I separate the admin models by models group (as everything)
#that's why I write smth like 'from api.models import subject as models'
#technically, every model is accessed from api.models __init__.py
#but I want to incapsulate, so I import only part of the models

#the order of models is the same as the order paths in urls