from rest_framework.views import APIView, Response, status
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permisions import IsStudent
from api.models import User, Student, Manual, Module, Topic, Task
from api.serializers import ProgressSerializer

@extend_schema(tags=['api / subject'])
class DetailedTaskView(APIView):
  queryset = Task.objects.all()
  serializer_class = ProgressSerializer
  permission_classes = [IsStudent]
  
  @extend_schema(request=None)
  def post(self, request, subject_slug, module_slug, topic_slug, slug, *args, **kwargs):
    user: User = request.user.user
    if user.student:
      student: Student = user.student
      subject = get_object_or_404(Manual, subject_slug)
      module = get_object_or_404(Module, subject=subject, slug=module_slug)
      topic = get_object_or_404(Topic, module=module, slug=topic_slug)
      task = get_object_or_404(self.queryset, topic=topic, slug=slug)
      if task not in student.completed_tasks.all():
        student.add_task_to_completed(task)
        return Response({
          'subject': student.calc_progress(subject),
          'module': student.calc_progress(module),
          'topic': student.calc_progress(topic),
        }, status.HTTP_200_OK)
    return Response({ 'subject': None, 'module': None, 'topic': None }, status.HTTP_204_NO_CONTENT)
