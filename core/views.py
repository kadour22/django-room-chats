from rest_framework import generics, permissions
from .models import Room, Message
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RoomSerializer, MessageSerializer


# class RegistrationView(generics.CreateAPIView):
#     serializer_class = RegistrationSerializer


# List all rooms or create a new room
class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

# Get details of a single room including messages
class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        room = self.get_object()
        # Get all messages in this room
        messages = Message.objects.filter(room=room).order_by("timestamp")
        message_serializer = MessageSerializer(messages, many=True)
        room_serializer = RoomSerializer(room)
        return Response({
            "room": room_serializer.data,
            "messages": message_serializer.data
        })


class MessageCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        room_id = request.data.get('room_id')
        content = request.data.get('content')
        room = Room.objects.get(id=room_id)

        message = Message.objects.create(
            room=room,
            user=request.user,
            content=content
        )
        serializer = MessageSerializer(message)
        return Response(serializer.data)
