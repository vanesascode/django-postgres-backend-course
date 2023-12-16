from rest_framework import serializers
from stateslist_app.models import State

class StateSerializer(serializers.ModelSerializer):
  
  length_address = serializers.SerializerMethodField() # calculated field
  class Meta:
    model = State
    fields = '__all__'
    # fields = ['id', 'address', 'description', 'active']
    # exclude = ['id']
    
  # 'Object' refers to a State model instance that is being serialized by the StateSerializer class.
  def get_length_address(self, object): # calculated field function
    return len(object.address)
    
  def validate(self, data):
    if data['address']==data['city']:
      raise serializers.ValidationError('Address and city must be different')
    else:
      return data
  
  def validate_image(self, value):
    if len(value) < 2:
      raise serializers.ValidationError('URL of image is too short. It must be at leas 2 characters')
    return value

# Notice this validation must be outside the class:
# def column_length(value):
#   if len(value) < 2:
#     raise serializers.ValidationError('Input is too short. It must be at leas 2 characters')

# class StateSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   address = serializers.CharField(validators=[column_length])
#   city = serializers.CharField(validators=[column_length])
#   description = serializers.CharField()
#   image = serializers.CharField()
#   active = serializers.BooleanField()
  
#   def create(self, validated_data):
#     return State.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#     instance.address = validated_data.get('address', instance.address)
#     instance.city = validated_data.get('city', instance.city)
#     instance.description = validated_data.get('description', instance.description)
#     instance.image = validated_data.get('image', instance.image)
#     instance.active = validated_data.get('active', instance.active)
#     instance.save()
#     return instance
  
#   # Notice these validations are inside the class. validate() is a preexisting method:
  
#   def validate(self, data):
#     if data['address']==data['city']:
#       raise serializers.ValidationError('Address and city must be different')
#     else:
#       return data
  
#   def validate_image(self, value):
#     if len(value) < 2:
#       raise serializers.ValidationError('URL of image is too short. It must be at leas 2 characters')
#     return value

  
