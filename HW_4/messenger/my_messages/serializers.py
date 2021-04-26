from rest_framework import serializers

from my_messages.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
