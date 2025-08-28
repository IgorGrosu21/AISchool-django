from django.utils.deprecation import MiddlewareMixin
from django.http import request, response

class AllowIframeForPDFsMiddleware(MiddlewareMixin):
  def process_response(self, request: request.HttpRequest, response: response.HttpResponse):
    if request.path.startswith('/public/theories/') and request.path.endswith('.pdf'):
      response['X-Frame-Options'] = 'ALLOWALL'
    
    return response