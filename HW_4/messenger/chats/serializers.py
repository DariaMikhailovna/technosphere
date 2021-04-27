from rest_framework import serializers

from chats.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Chat
        fields = ['title', 'created_date', 'author', 'participants', 'pk']
