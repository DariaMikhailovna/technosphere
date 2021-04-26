from chats.models import Chat
from chats.serializers import ChatSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class ChatViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Chat.objects.all()
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)
