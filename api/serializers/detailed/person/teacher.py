from api.models import SubjectName, School, Position

from ...name import SubjectNameSerializer
from ...listed import PositionSerializer, TeacherSerializer
from .person import DetailedPersonSerializer

class DetailedTeacherSerializer(DetailedPersonSerializer, TeacherSerializer):
  subject_names = SubjectNameSerializer(required=False, allow_null=True, many=True)
  work_places = PositionSerializer(required=False, allow_null=True, many=True)
  
  class Meta(TeacherSerializer.Meta):
    fields = TeacherSerializer.Meta.fields + ['user', 'experience', 'subject_names', 'work_places']
  
  def get_subject_names(self, validated_data):
    subject_names_data = validated_data.pop('subject_names')
    return SubjectName.objects.filter(id__in=map(lambda entry: entry.get('id'), subject_names_data)), validated_data
  
  def get_work_places(self, teacher, validated_data):
    work_places_data = validated_data.pop('work_places')
    Position.objects.filter(teacher=teacher).exclude(id__in=map(lambda entry: entry.get('id'), work_places_data)).delete()
    work_places = []
    for work_place_data in work_places_data:
      subject_names, work_place_data = self.get_subject_names(work_place_data)
      id = work_place_data.pop('id')
      school, type = School.objects.get(id=work_place_data.pop('school').get('id')), work_place_data.pop('type')
      if id != '':
        work_places_qs = Position.objects.filter(id=id)
        work_places_qs.update(teacher=teacher, school=school, type=type)
        work_place = work_places_qs.first()
      else:
        work_place = Position.objects.create(teacher=teacher, school=school, type=type)
      if type == 'HM':
        work_place.is_manager = True
        work_place.save()
      work_place.subject_names.set(subject_names)
      work_places.append(work_place)
    return work_places, validated_data
  
  def update(self, teacher, validated_data):
    subject_names, validated_data = self.get_subject_names(validated_data)
    teacher.subject_names.set(subject_names)
    _, validated_data = self.get_work_places(teacher, validated_data)
    
    return super().update(teacher, validated_data)