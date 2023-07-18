from rest_framework import serializers
from core.models import UserAction


class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = ['id', 'user', 'action', 'numbers', 'numbers_sets',
                  'time_duration', 'time_created', 'time_updated']
