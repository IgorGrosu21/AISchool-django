from ...name import SubjectNameSerializer
from ...listed import PositionSerializer, TeacherSerializer
from ..lesson import DetailedHomeworkSerializer
from .person import DetailedPersonSerializer, PersonHomeSerializer
from .timetable import TomorrowTimetableSerializer
from .analytics import TeacherAnalyticsSerializer

class DetailedTeacherSerializer(DetailedPersonSerializer, TeacherSerializer):
  subjects = SubjectNameSerializer(many=True)
  work_places = PositionSerializer(many=True)

  class Meta(TeacherSerializer.Meta):
    fields = TeacherSerializer.Meta.fields + ['user', 'experience', 'subjects', 'work_places']
    nested_fields = {
      'one': {
        **TeacherSerializer.Meta.nested_fields.get('one', {}),
      },
      'many': {
        **TeacherSerializer.Meta.nested_fields.get('many', {}),
        'subjects': 'retrieve',
        'work_places': 'mutate'
      },
    }

class TeacherHomeSerializer(PersonHomeSerializer):
  latest_homeworks = DetailedHomeworkSerializer(many=True, read_only=True)
  tomorrow_timetable = TomorrowTimetableSerializer(many=True, read_only=True)
  analytics = TeacherAnalyticsSerializer(many=True, read_only=True)

  class Meta(TeacherSerializer.Meta):
    fields = PersonHomeSerializer.Meta.fields + ['latest_homeworks', 'tomorrow_timetable', 'analytics']