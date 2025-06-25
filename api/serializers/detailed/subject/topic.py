from rest_framework.serializers import SerializerMethodField

from api.models import User, Student

from .progress import ProgressSerializer
from ...listed import TopicSerializer, ModuleWithSubjectSerializer, TaskSerializer, TheorySerializer

class DetailedTopicSerializer(ProgressSerializer, TopicSerializer):
  module = ModuleWithSubjectSerializer()
  theories = TheorySerializer(many=True)
  tasks = TaskSerializer(many=True)
  completed_theories = SerializerMethodField()
  completed_tasks = SerializerMethodField()
  
  def get_completed_priceables(self, priceables_name: str, obj):
    user: User = self.context['request'].user.user
    if user.student:
      student: Student = user.student
      priceables = student.get_priceables(priceables_name)
      return list(priceables.filter(topic=obj).values_list('slug', flat=True))
    return []
  
  def get_completed_theories(self, obj):
    return self.get_completed_priceables('theories', obj)
  
  def get_completed_tasks(self, obj):
    return self.get_completed_priceables('tasks', obj)
  
  class Meta(TopicSerializer.Meta):
    fields = TopicSerializer.Meta.fields + ProgressSerializer.Meta.fields + ['module', 'theories', 'tasks', 'completed_theories', 'completed_tasks']