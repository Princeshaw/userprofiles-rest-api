from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializers a name fiel for testing our APIView"""
    name = serializers.CharField(max_length=10)