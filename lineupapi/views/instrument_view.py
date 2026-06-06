from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from lineupapi.models import Instrument
from rest_framework import status


class InstrumentSerializer(ModelSerializer):
    
    class Meta:
        model = Instrument
        fields = ('id', 'name')


class InstrumentView(ViewSet): 

    def list(self, request):
        instruments = Instrument.objects.all()
        serialized = InstrumentSerializer(instruments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    

    def retrieve (self, request, pk=None):
        instrument = Instrument.objects.get(pk=pk)
        serialized = InstrumentSerializer(instrument)
        return Response(serialized.data, status=status.HTTP_200_OK)
        
    
    "There will be no ability to create, update, or delete instruments. These will be seeded in the database and only read by the client."
