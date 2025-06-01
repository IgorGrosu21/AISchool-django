from api.models import Position

from ..can_edit import CanEditSerializer
from ...media import DetailedMediaSerializer
from ...listed import PositionSerializer, KlassSerializer, SchoolSerializer

class DetailedSchoolSerializer(SchoolSerializer, CanEditSerializer):
  staff = PositionSerializer(many=True)
  klasses = KlassSerializer(many=True, read_only=True)
  photos = DetailedMediaSerializer(many=True, read_only=True)
  
  class Meta(SchoolSerializer.Meta):
    fields = SchoolSerializer.Meta.fields + ['desc', 'phones', 'emails', 'work_hours', 'staff', 'klasses', 'photos']
  
  def get_staff(self, school, validated_data):
    positions_data = validated_data.pop('staff')
    Position.objects.filter(school=school).exclude(id__in=map(lambda entry: entry.get('id'), positions_data)).delete()
    positions = Position.objects.none()
    for position_data in positions_data:
      id = position_data.pop('id')
      positions_qs = Position.objects.filter(id=id)
      positions_qs.update(type=position_data.pop('type'), is_manager=position_data.pop('is_manager'))
      positions |= positions_qs
    return positions, validated_data
  
  def update(self, school, validated_data):
    _, validated_data = self.get_staff(school, validated_data)
    
    return super().update(school, validated_data)
  
  def to_representation(self, instance):
    r = super().to_representation(instance)
    try:
      user = self.context['request'].user.user
      r['can_edit'] = user.id in instance.managers.values_list('teacher__user__id', flat=True)
    finally:
      return r