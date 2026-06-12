from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User

from lineupapi.models import Profile, Instrument
from rest_framework import status




class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class InstrumentSerializer(ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name')


class ProfileSerializer(ModelSerializer):
    user = UserSerializer(many=False)
    instruments = InstrumentSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'soundcloud', 'instagram', 'instruments')




class ProfileView(ViewSet):
    #List all profiles. Need this on client side Musicians Page
    def list(self, request):
        profiles = Profile.objects.all()
        instrument_id = request.query_params.get('instrument_id')
        if instrument_id:
            profiles = profiles.filter(instruments__id=instrument_id)
        serialized = ProfileSerializer(profiles, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    #Retrieve a single profile by id. Need this for showing a musician's profile single detail page
    def retrieve(self, request, pk=None):
        profile = Profile.objects.get(pk=pk)
        serialized = ProfileSerializer(profile)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    #Get or update the current user's profile. Need this for showing the current user's profile page and allowing them to edit it.
    @action(detail=False, methods=['get', 'patch'], url_path='me')
    def me(self, request):
        profile = Profile.objects.get(user=request.user)

        if request.method == 'PATCH':
            profile.bio = request.data.get('bio', profile.bio)
            profile.soundcloud = request.data.get('soundcloud', profile.soundcloud)
            profile.instagram = request.data.get('instagram', profile.instagram)
            profile.save()
            if 'instruments' in request.data:
                profile.instruments.set(request.data['instruments'])

        serialized = ProfileSerializer(profile)
        return Response(serialized.data, status=status.HTTP_200_OK)

    #Create a profile for the current user. This will only be used once, when the user first creates their profile.
    def create(self, request):
        user = request.user
        profile = Profile.objects.create(
            user=user,
            bio=request.data.get('bio', ''),
            soundcloud=request.data.get('soundcloud', ''),
            instagram=request.data.get('instagram', '')
        )
        serialized = ProfileSerializer(profile)
        return Response(serialized.data, status=status.HTTP_201_CREATED)