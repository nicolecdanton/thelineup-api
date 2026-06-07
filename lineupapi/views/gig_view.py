from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from lineupapi.models import Gig
from rest_framework import status

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class GigSerializer(ModelSerializer):
    booker = UserSerializer(many=False)
    class Meta:
        model = Gig
        fields = ('id', 'booker', 'title', 'date', 'time', 'venue', 'pay_per_musician', 'description')



class GigView(ViewSet):

    def list(self, request):
        gigs = Gig.objects.all()
        serialized = GigSerializer(gigs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    

    def retrieve(self, request, pk=None):
        gig = Gig.objects.get(pk=pk)
        serialized = GigSerializer(gig)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        booker = request.user
        gig = Gig.objects.create(
            booker=booker,
            title=request.data['title'],
            date=request.data['date'],
            time=request.data['time'],
            venue_id=request.data['venue_id'],
            pay_per_musician=request.data['pay_per_musician'],
            description=request.data['description']
        )
        serialized = GigSerializer(gig)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        gig = Gig.objects.get(pk=pk)
        gig.title = request.data['title']
        gig.date = request.data['date']
        gig.time = request.data['time']
        gig.venue_id = request.data['venue_id']
        gig.pay_per_musician = request.data['pay_per_musician']
        gig.description = request.data['description']
        gig.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        gig = Gig.objects.get(pk=pk)
        gig.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)