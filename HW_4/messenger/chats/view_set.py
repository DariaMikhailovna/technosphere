from chats.models import Chat
from chats.serializers import ChatSerializer

from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


# class ChatViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Chat.objects.all()
#         serializer = ChatSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Chat.objects.all()
#         chat = get_object_or_404(queryset, pk=pk)
#         serializer = ChatSerializer(chat)
#         return Response(serializer.data)


class NewChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    permission_classes = []
