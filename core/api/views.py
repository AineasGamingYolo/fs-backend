from django.http import HttpResponseRedirect
#from django.contrib.auth.models import User
from core.models import CustomUser
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from core.api.serializers import UserSerializer, UserSerializerWithToken, RegisterSerializer
from rest_framework import serializers, generics
from rest_framework.permissions import AllowAny

# @api_view(['GET'])
# def current_user(request):
#     """
#     Determine the current user by their token, and return their data
#     """
    
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
