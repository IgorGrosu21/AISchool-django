from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView, Response, Request, status
from rest_framework.exceptions import ParseError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from auth.serializers import AccessTokenSerializer

class WithValidRefreshTokenView(APIView):
  def post(self, request: Request, *args, **kwargs):
    refresh_token = request.data.get('refresh')
    if not refresh_token:
      raise ParseError(code='no_refresh_token')

    try:
      refresh = RefreshToken(refresh_token)
      return refresh
    except Exception as e:
      raise ParseError(code='invalid_refresh_token') from e

class RefreshTokenView(WithValidRefreshTokenView):
  authentication_classes = []
  permission_classes = []

  @extend_schema(tags=['auth / refresh'], request=None, responses={
    status.HTTP_200_OK: AccessTokenSerializer
  })
  def post(self, request, *args, **kwargs):
    refresh = super().post(request, *args, **kwargs)
    access = refresh.access_token
    return Response({'access': str(access)}, status=status.HTTP_200_OK)

class LogoutView(WithValidRefreshTokenView):
  @extend_schema(tags=['auth / refresh'], request=None, responses={
    status.HTTP_204_NO_CONTENT: None
  })
  def post(self, request, *args, **kwargs):
    refresh = super().post(request, *args, **kwargs)
    refresh.blacklist()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class LogoutAllView(APIView):
  @extend_schema(tags=['auth / refresh'], request=None, responses={
    status.HTTP_204_NO_CONTENT: None
  })
  def post(self, request: Request):
    #get existing tokens for current user
    tokens = OutstandingToken.objects.filter(user=request.user)

    #get already banned tokens
    blacklisted_token_ids = set(BlacklistedToken.objects.filter(token__in=tokens).values_list('token_id', flat=True))

    #ban every token that isn't already banned
    new_blacklist =  [BlacklistedToken(token=token) for token in tokens if token.id not in blacklisted_token_ids]

    #save newly banned tokens
    BlacklistedToken.objects.bulk_create(new_blacklist, ignore_conflicts=True)
    return Response(None, status=status.HTTP_204_NO_CONTENT)