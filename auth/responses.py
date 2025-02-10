from rest_framework.response import Response
from core.settings import SIMPLE_JWT
from rest_framework import status

class EmailAlreadyRegistered(Response):
  def __init__(self):
    super().__init__('registered', status=status.HTTP_400_BAD_REQUEST)
    
class UserNotFound(Response):
  def __init__(self):
    super().__init__('unfound', status=status.HTTP_404_NOT_FOUND)
    
class IncorrectPassword(Response):
  def __init__(self):
    super().__init__('incorect', status=status.HTTP_401_UNAUTHORIZED)
    
class MailServerError(Response):
  def __init__(self):
    super().__init__('mail_error', status=status.HTTP_503_SERVICE_UNAVAILABLE)

class CodeInvalid(Response):
  def __init__(self):
    super().__init__('code_invalid', status=status.HTTP_401_UNAUTHORIZED)

class Succes(Response):
  def __init__(self, access_token='success'):
    super().__init__(str(access_token), status=status.HTTP_200_OK)
    
class Unauthorized(Response):
  def __init__(self):
    super().__init__('unauthorized', status=status.HTTP_401_UNAUTHORIZED)