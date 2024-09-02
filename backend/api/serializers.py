"""Test."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Test."""

    class Meta:
        """Test."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
