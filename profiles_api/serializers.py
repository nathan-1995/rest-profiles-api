from rest_framework import serializers


class HelloSerializers(serializers.Serializer):

    """Serializer a name field for testing our apiview"""
    name = serializers.CharField(max_length=10)
    #age = serializers.IntegerField()
