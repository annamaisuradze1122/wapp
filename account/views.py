from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserRegistrationSerializer
from .models import User
from django.http import HttpResponseRedirect
from rest_framework import permissions, decorators



@api_view(['POST'])
def registration(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    serializer = UserSerializer(serializer.user)
    return Response(serializer.data, status=201)


@api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def logout(request):
    return HttpResponseRedirect("/")

