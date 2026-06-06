from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from lineupapi.models import Venue
from rest_framework import status

class VenueSerializer(ModelSerializer):
    
    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'city', 'state')


class VenueView(ViewSet):

    def list(self, request):
        venues = Venue.objects.all()
        serialized = VenueSerializer(venues, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    

    def retrieve (self, request, pk=None):
        venue = Venue.objects.get(pk=pk)
        serialized = VenueSerializer(venue)
        return Response(serialized.data, status=status.HTTP_200_OK)
        
    "There will be no ability to create, update, or delete venues. These will be seeded in the database and only read by the client."