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
    #List gigs created by current user- for showing 'My Gigs' on the client side
    def list(self, request):
        gigs = Gig.objects.filter(booker=request.user)
        serialized = GigSerializer(gigs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    #Retrieve a single gig by id
    def retrieve(self, request, pk=None):
        gig = Gig.objects.get(pk=pk)
        serialized = GigSerializer(gig)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    #Create a new gig. The booker is the current user.
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
    
    #Update an existing gig. Only the booker can update the gig.
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
    
    #Delete a gig. Only the booker can delete the gig.
    def destroy(self, request, pk=None):
        gig = Gig.objects.get(pk=pk)
        gig.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)