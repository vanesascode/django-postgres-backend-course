from rest_framework.response import Response
from stateslist_app.models import State
from stateslist_app.api.serializers import StateSerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# OPTION WITH CLASS APIView - Model of classes:

class StateListApiView(APIView):
  def get(self, request):
    states = State.objects.all()
    serializer = StateSerializer(states, many=True) #many=True tells the serializer to expect a list of objects instead of a single object
    return Response(serializer.data)
  
  def post(self, request):
    de_serializer = StateSerializer(data=request.data)
    if de_serializer.is_valid():
      de_serializer.save()
      return Response(de_serializer.data)
    else:
      return Response(de_serializer.errors, state=status.HTTP_400_BAD_REQUEST)
    
class StateDetailApiView(APIView):
  def get(self, request, pk):
    try:
      state = State.objects.get(pk=pk)
    except State.DoesNotExist:
      return Response({'Error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StateSerializer(state)
    return Response(serializer.data)
    
  def put(self, request, pk):
    try:
      state = State.objects.get(pk=pk)
    except State.DoesNotExist:
      return Response({'Error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
    
    de_serializer = StateSerializer(state, data=request.data)
    if de_serializer.is_valid():
      de_serializer.save()
      return Response(de_serializer.data)
    else:
      return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    try:
      state = State.objects.get(pk=pk)
    except State.DoesNotExist:
      return Response({'Error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
    
    state.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# OPTION WITH DECORATORS - Model of functions: 

# @api_view(['GET', 'POST'])
# def states_list(request):
#   if request.method == 'GET':
#     states = State.objects.all()
#     serializer = StateSerializer(states, many=True) 
#     return Response(serializer.data)
  
#   if request.method == 'POST':
#     de_serializer = StateSerializer(data=request.data)
#     if de_serializer.is_valid():
#       de_serializer.save()
#       return Response(de_serializer.data)
#     else:
#       return Response(de_serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE']) 
# def state_details(request, pk):
#   if request.method == 'GET':
#     try:
#       state = State.objects.get(pk=pk)
#       serializer = StateSerializer(state)
#       return Response(serializer.data)
#     except State.DoesNotExist:
#       return Response({'Error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
        
#   if request.method == 'PUT':
#     state = State.objects.get(pk=pk)
#     de_serializer = StateSerializer(state, data=request.data)
#     if de_serializer.is_valid():
#       de_serializer.save()
#       return Response(de_serializer.data)
#     else:
#       return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   if request.method == 'DELETE':
#     try:
#       state = State.objects.get(pk=pk)
#       state.delete()
#     except State.DoesNotExist:
#       return Response({'Error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
#     return Response(status=status.HTTP_204_NO_CONTENT)