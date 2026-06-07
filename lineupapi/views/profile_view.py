from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from lineupapi.models import Profile
from rest_framework import status




class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ProfileSerializer(ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'soundcloud', 'instagram')


class ProfileView(ViewSet):

    def list(self, request):
        profiles = Profile.objects.all()
        serialized = ProfileSerializer(profiles, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    

    def retrieve(self, request, pk=None):
        profile = Profile.objects.get(pk=pk)
        serialized = ProfileSerializer(profile)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user = request.user
        profile = Profile.objects.create(
            user=user,
            bio=request.data['bio'],
            soundcloud=request.data['soundcloud'],
            instagram=request.data['instagram']
        )
        serialized = ProfileSerializer(profile)
        return Response(serialized.data, status=status.HTTP_201_CREATED)