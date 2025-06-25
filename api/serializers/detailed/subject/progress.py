from rest_framework.serializers import ModelSerializer, SerializerMethodField

from api.models import User, Student

class ProgressSerializer(ModelSerializer):
  progress = SerializerMethodField()
  
  def get_progress(self, obj):
    user: User = self.context['request'].user.user
    if user.student:
      student: Student = user.student
      return student.calc_progress(obj)
    return None
  
  class Meta:
    fields = ['progress']