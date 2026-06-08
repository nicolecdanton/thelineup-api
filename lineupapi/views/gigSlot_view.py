
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from lineupapi.models import Gig, Instrument, GigSlot
from rest_framework import status

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class GigSerializer(ModelSerializer):
    booker = UserSerializer(many=False)
    class Meta:
        model = Gig
        fields = ('id', 'booker', 'title', 'date', 'time', 'venue', 'pay_per_musician', 'description')

class InstrumentSerializer(ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name']

class GigSlotSerializer(ModelSerializer):
    gig = GigSerializer(many=False)
    instrument = InstrumentSerializer(many=False)
    filled_by = UserSerializer(many=False)
    class Meta:
        model = GigSlot
        fields = ('id', 'gig', 'instrument', 'filled_by')

class GigSlotView(ViewSet):
    #Lists all of the slots for a specific gig
    def list(self, request):
        gig_id = request.query_params.get('gig_id')
        gig_slots = GigSlot.objects.filter(gig_id=gig_id)
        serialized = GigSlotSerializer(gig_slots, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    #Get a single slot by id
    def retrieve(self, request, pk=None):
        try:
            gig_slot = GigSlot.objects.get(pk=pk)
        except GigSlot.DoesNotExist:
            return Response({'error': 'GigSlot not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = GigSlotSerializer(gig_slot)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        gig_slot = GigSlot.objects.create(
            gig_id=request.data['gig_id'],
            instrument_id=request.data['instrument_id']
        )
        serialized = GigSlotSerializer(gig_slot)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        try:
            gig_slot = GigSlot.objects.get(pk=pk)
        except GigSlot.DoesNotExist:
            return Response({'error': 'GigSlot not found'}, status=status.HTTP_404_NOT_FOUND)
        gig_slot.gig_id = request.data['gig_id']
        gig_slot.instrument_id = request.data['instrument_id']
        gig_slot.filled_by_id = request.data['filled_by_id']
        gig_slot.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)