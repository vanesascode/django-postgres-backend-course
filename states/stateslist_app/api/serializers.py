from rest_framework import serializers
from stateslist_app.models import State

def column_length(value):
  if len(value) < 2:
    raise serializers.ValidationError('Address is too short')

class StateSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  address = serializers.CharField(validators=[column_length])
  city = serializers.CharField()
  description = serializers.CharField()
  image = serializers.CharField()
  active = serializers.BooleanField()
  
  def create(self, validated_data):
    return State.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.address = validated_data.get('address', instance.address)
    instance.city = validated_data.get('city', instance.city)
    instance.description = validated_data.get('description', instance.description)
    instance.image = validated_data.get('image', instance.image)
    instance.active = validated_data.get('active', instance.active)
    instance.save()
    return instance

  
