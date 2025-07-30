from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

@extend_schema(exclude=True)
class WorkerView(APIView):
  authentication_classes = []
  permission_classes = []
  
  def get(self, request):
    return Response()