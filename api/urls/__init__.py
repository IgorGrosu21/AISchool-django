from .country import country_urlpatterns
from .lesson import lesson_urlpatterns
from .manual import manual_urlpatterns
from .person import person_urlpatterns
from .school import school_urlpatterns
from .subject import subject_urlpatterns
from .user import user_urlpatterns
from .worker import worker_urlpatterns

urlpatterns = (
  country_urlpatterns +
  lesson_urlpatterns +
  manual_urlpatterns +
  person_urlpatterns +
  subject_urlpatterns +
  school_urlpatterns +
  user_urlpatterns +
  worker_urlpatterns
)

#I separate the url_patterns by models group (as everything)
#that's why I write smth like 'from api.views import subject as views'
#technically, every view is accessed from api.views __init__.py
#but I want to incapsulate, so I import only part of the views