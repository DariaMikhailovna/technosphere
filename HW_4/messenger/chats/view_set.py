from chats.models import Chat
from chats.serializers import ChatSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def check_login(func):
    def wrapper(*args, **kwargs):
        if args[1].user.is_authenticated:
            return func(*args, **kwargs)
        else:
            print('NOT AUTHENTICATED')
            return redirect('/login/')
    return wrapper


class ChatViewSet(viewsets.ViewSet):
    queryset = Chat.objects.all()

    def list(self, request):
        serializer = ChatSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @check_login
    def retrieve(self, request, pk=None):
        chat = get_object_or_404(self.queryset, pk=pk)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    @check_login
    def create(self, request):
        print('AAAAAAA')
        chat = Chat()
        chat.author_id = request.POST['user']
        chat.created_date = timezone.now()
        chat.save()

    @check_login
    def update(self, request, pk=None):
        pass

    @check_login
    def destroy(self, request, pk=None):
        pass


class NewChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    permission_classes = []
