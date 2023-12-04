from rest_framework import serializers

class StateSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  address = serializers.CharField()
  city = serializers.CharField()
  description = serializers.CharField()
  image = serializers.CharField()
  active = serializers.BooleanField()