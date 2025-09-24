from rest_framework.serializers import SerializerMethodField

from api.models import User, Student

from .progress import ProgressSerializer
from ...listed import TopicSerializer, ModuleWithManualSerializer, TaskSerializer, TheorySerializer

class DetailedTopicSerializer(ProgressSerializer, TopicSerializer):
  module = ModuleWithManualSerializer()
  theories = TheorySerializer(many=True)
  tasks = TaskSerializer(many=True)
  completed_tasks = SerializerMethodField()

  def get_completed_tasks(self, obj) -> list[str]:
    user: User = self.context['request'].user.user
    if user.student:
      student: Student = user.student
      return list(student.completed_tasks.filter(topic=obj).values_list('slug', flat=True))
    return []

  class Meta(TopicSerializer.Meta):
    fields = TopicSerializer.Meta.fields + ['progress', 'module', 'theories', 'tasks', 'completed_tasks']