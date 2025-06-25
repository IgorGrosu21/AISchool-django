from rest_framework.serializers import SerializerMethodField

from api.models import User, Klass, School

from ..can_edit import CanEditSerializer
from ...listed import SocialSerializer, CitySerializer, UserSerializer

from ..._helpers import EditableSerializer

class DetailedUserSerializer(UserSerializer, EditableSerializer, CanEditSerializer):
  socials = SocialSerializer(many=True)
  city = CitySerializer()
  
  class Meta(UserSerializer.Meta):
    fields = UserSerializer.Meta.fields + ['socials', 'city', 'lang', 'can_edit']
    nested_fields = {
      'one': {
        'city': 'retrieve'
      },
      'many': {
        'socials': 'mutate'
      }
    }
    
class UserRoutesSerializer(UserSerializer):
  is_account_verified = SerializerMethodField()
  klass_link = SerializerMethodField()
  school_link = SerializerMethodField()
  diary_link = SerializerMethodField()
  journal_link = SerializerMethodField()
  
  def get_is_account_verified(self, obj: User):
    return obj.account.is_verified
  
  @UserSerializer.handle_staff
  def get_klass_link(self, obj: User):
    if obj.account.is_staff:
      return None
    if obj.is_teacher:
      klass: Klass | None = obj.teacher.klass if hasattr(obj.teacher, 'klass') else None
    else:
      klass: Klass | None = obj.student.klass
    if klass:
      return f'schools/{klass.school.id}/klasses/{klass.id}'
  
  @UserSerializer.handle_staff
  def get_school_link(self, obj: User):
    if obj.account.is_staff:
      return None
    if obj.is_teacher:
      school: School | None = obj.teacher.work_places.first().school if obj.teacher.work_places.exists() else None
    else:
      school: School | None = obj.student.klass.school
    if school:
      return f'schools/{school.id}'
  
  @UserSerializer.handle_staff
  def get_diary_link(self, obj: User):
    if obj.account.is_staff:
      return None
    if obj.is_teacher:
      school = obj.teacher.work_places.first().school if obj.teacher.work_places.exists() else None
      return f'diary/{school.id}' if school else None
    klass: Klass | None = obj.student.klass
    return f'diary/{klass.school.id}/{klass.id}' if klass else None
  
  @UserSerializer.handle_staff
  def get_journal_link(self, obj: User):
    if obj.account.is_staff:
      return None
    if obj.is_teacher:
      school = obj.teacher.work_places.first().school if obj.teacher.work_places.exists() else None
      return f'journal/{school.id}' if school else None
    klass: Klass | None = obj.student.klass
    return f'journal/{klass.school.id}/{klass.id}' if klass else None
  
  class Meta(UserSerializer.Meta):
    fields = UserSerializer.Meta.fields + ['is_account_verified', 'klass_link', 'school_link', 'diary_link', 'journal_link']
    nested_fields = {
      'one': {
        'city': 'retrieve'
      },
      'many': {
        'socials': 'mutate'
      }
    }