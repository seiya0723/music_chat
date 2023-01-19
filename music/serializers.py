from rest_framework import serializers
from .models import DirectMessage

class DirectMessageSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    #receiver = MatchingFilter()

    class Meta:
        model = DirectMessage
        fields = ('id', 'sender', 'receiver', 'message', 'created_at')
        extra_kwargs = {'sender': {'read_only': True}}
