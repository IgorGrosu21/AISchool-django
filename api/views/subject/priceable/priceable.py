from rest_framework.views import APIView, Response, status
from django.db.models import QuerySet

from api.models import User, Student, Subject, Module, Topic
    
class DetailedPriceableView(APIView):
  queryset: QuerySet
  priceables_name: str
  
  def put(self, request, subject_slug, module_slug, topic_slug, slug, *args, **kwargs):
    user: User = request.user.user
    if user.student:
      student: Student = user.student
      subject = Subject.objects.get(slug=subject_slug)
      module = Module.objects.get(subject=subject, slug=module_slug)
      topic = Topic.objects.get(module=module, slug=topic_slug)
      priceable = self.queryset.get(topic=topic, slug=slug)
      manager = student.get_priceables(self.priceables_name)
      if priceable not in manager.all():
        student.add_priceable(priceable)
        return Response({
          'subject': student.calc_progress(subject),
          'module': student.calc_progress(module),
          'topic': student.calc_progress(topic),
        }, status.HTTP_200_OK)
    return Response({ 'subject': None, 'module': None, 'topic': None }, status.HTTP_406_NOT_ACCEPTABLE)
