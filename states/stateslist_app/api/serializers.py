from rest_framework import serializers
from stateslist_app.models import State
from stateslist_app.models import Business
from stateslist_app.models import Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
    
class StateSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
  length_address = serializers.SerializerMethodField() # calculated field
  class Meta:
    model = State
    fields = '__all__'
    # fields = ['id', 'address', 'description', 'active']
    # exclude = ['id']
    
    
  # 'Object' refers to a State model instance that is being serialized by the StateSerializer class.
  def get_length_address(self, object): # calculated field function
    return len(object.address)

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
# class BusinessSerializer(serializers.ModelSerializer):
  stateslist = StateSerializer(many=True, read_only=True)
  # stateslist = serializers.StringRelatedField(many=True)
  # stateslist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  # stateslist =  serializers.HyperlinkedRelatedField(
  #   many=True, 
  #   read_only=True, 
  #   view_name='state-details' # this is the name we used in the path of the urlpatterns, to get one onlystate
  #   )
  class Meta:
    model = Business
    fields = '__all__'
    

    
    
    
    
  # def validate(self, data):
  #   if data['address']==data['city']:
  #     raise serializers.ValidationError('Address and city must be different')
  #   else:
  #     return data
  
  # def validate_image(self, value):
  #   if len(value) < 2:
  #     raise serializers.ValidationError('URL of image is too short. It must be at leas 2 characters')
  #   return value

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

  
