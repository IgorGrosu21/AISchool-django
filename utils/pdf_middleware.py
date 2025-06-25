from django.utils.deprecation import MiddlewareMixin

class AllowIframeForPDFsMiddleware(MiddlewareMixin):
  def process_response(self, request, response):
    if request.path.startswith('/media/') and request.path.endswith('.pdf'):
      response['X-Frame-Options'] = 'ALLOWALL'
    return response