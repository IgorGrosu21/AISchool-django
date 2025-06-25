ADMIN_REORDER = (
  { 'app': 'api', 'label': 'Страны', 'models': (
    'api.City', 'api.Country', 'api.Region'
  ) },
  { 'app': 'api', 'label': 'Дневник', 'models': (
    'api.HomeworkPhoto', 'api.Homework', 'api.LessonTime', 'api.Lesson', 'api.Note', 'api.SpecificLessonPhoto', 'api.SpecificLesson'
  ) },
  { 'app': 'api', 'label': 'Модули', 'models': (
    'api.Task', 'api.Theory', 'api.ModuleProgress', 'api.Module', 'api.Topic'
  ) },
  { 'app': 'api', 'label': 'Люди', 'models': (
    'api.Balance', 'api.Student', 'api.Subscription', 'api.Teacher'
  ) },
  { 'app': 'api', 'label': 'Школы', 'models': (
    'api.Klass', 'api.Position', 'api.SchoolPhoto', 'api.School'
  ) },
  { 'app': 'api', 'label': 'Предметы', 'models': (
    'api.SubjectName', 'api.SubjectType', 'api.Subject'
  ) },
  { 'app': 'api', 'label': 'Пользователи', 'models': (
    'api.Social', 'api.User'
  ) },
  { 'app': 'authentication', 'label': 'Аутентификация' },
  { 'app': 'auth', 'label': 'Авторизация' },
  { 'app': 'token_blacklist', 'label': 'Заблокированные Токены' }
)