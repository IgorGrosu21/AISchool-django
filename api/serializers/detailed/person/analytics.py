from rest_framework.serializers import Serializer, DateField, CharField, ListField

from ...name import SubjectNameSerializer, SchoolNameSerializer

#student
class PointSerializer(Serializer):
  date = DateField(format='%Y.%m.%d', input_formats=['%Y.%m.%d'], read_only=True)
  value = CharField(max_length=2, read_only=True)

class StudentAnalyticsSerializer(Serializer):
  subject = SubjectNameSerializer(read_only=True)
  points = PointSerializer(many=True, read_only=True)


#teacher
class AnalyticsByKlassSerializer(Serializer):
  slug = CharField(read_only=True, max_length=3)
  values = ListField(read_only=True, child=CharField(max_length=2))

class AnalyticsBySubjectSerializer(Serializer):
  subject_name = SubjectNameSerializer(read_only=True)
  klasses = AnalyticsByKlassSerializer(many=True, read_only=True)

class TeacherAnalyticsSerializer(Serializer):
  school = SchoolNameSerializer(read_only=True)
  subjects = AnalyticsBySubjectSerializer(many=True, read_only=True)
  