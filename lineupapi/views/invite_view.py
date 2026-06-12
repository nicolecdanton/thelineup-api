from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from lineupapi.views.gigSlot_view import GigSlotSerializer

from lineupapi.models import Invite
from rest_framework import status

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class InviteSerializer(ModelSerializer):
    slot = GigSlotSerializer(many=False)
    musician = UserSerializer(many=False)
    class Meta:
        model = Invite
        fields = ('id', 'slot', 'musician', 'status', 'sent_at', 'responded_at')



class InviteView(ViewSet):
    #current user's incoming invites
    def list(self, request):
        invites = Invite.objects.filter(musician=request.user)
        serialized = InviteSerializer(invites, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    
    def create(self, request):
        invite = Invite.objects.create(
            slot_id=request.data['slot_id'],
            musician_id=request.data['musician_id'],
            status='pending'
        )
        serialized = InviteSerializer(invite)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        invite = Invite.objects.get(pk=pk)
        invite.status = request.data['status']
        invite.responded_at = request.data['responded_at']
        invite.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
