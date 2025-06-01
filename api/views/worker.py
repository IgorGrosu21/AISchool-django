from rest_framework.views import APIView, Response
from api import models

# Create your views here.
class WorkerView(APIView):
  authentication_classes = []
  permission_classes = []
  
  def get(self, request, *args, **kwargs):
    return Response()