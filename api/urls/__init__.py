from .country import country_urlpatterns
from .person import person_urlpatterns
from .school import school_urlpatterns
from .subject import subject_urlpatterns
from .user import user_urlpatterns
from .worker import worker_urlpatterns

urlpatterns = (
  country_urlpatterns +
  person_urlpatterns +
  subject_urlpatterns +
  school_urlpatterns +
  user_urlpatterns +
  worker_urlpatterns
)
