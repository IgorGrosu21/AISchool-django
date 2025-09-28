ADMIN_REORDER = (
  { 'app': 'api', 'label': 'Страны', 'models': (
    'api.City', 'api.Country', 'api.Region'
  ) },
  { 'app': 'api', 'label': 'Дневник', 'models': (
    'api.HomeworkPhoto', 'api.Homework', 'api.LessonTime', 'api.Lesson', 'api.Note', 'api.SpecificLessonPhoto', 'api.SpecificLesson'
  ) },
  { 'app': 'api', 'label': 'Учебники', 'models': (
    'api.Balance', 'api.Manual', 'api.Module', 'api.Task', 'api.Topic'
  ) },
  { 'app': 'api', 'label': 'Люди', 'models': (
    'api.Parent', 'api.Student', 'api.Subscription', 'api.Teacher'
  ) },
  { 'app': 'api', 'label': 'Школы', 'models': (
    'api.Group', 'api.Klass', 'api.Position', 'api.SchoolPhoto', 'api.School'
  ) },
  { 'app': 'api', 'label': 'Предметы', 'models': (
    'api.Subject', 'api.SubjectType', 
  ) },
  { 'app': 'api', 'label': 'Пользователи', 'models': (
    'api.Social', 'api.User'
  ) },
  { 'app': 'authentication', 'label': 'Аутентификация' },
  { 'app': 'token_blacklist', 'label': 'Заблокированные Токены' }
)