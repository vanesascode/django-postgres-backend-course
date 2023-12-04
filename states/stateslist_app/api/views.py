from rest_framework.response import Response
from stateslist_app.models import State
from stateslist_app.api.serializers import StateSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def states_list(request):
  if request.method == 'GET':
    states = State.objects.all()
    serializer = StateSerializer(states, many=True) #many=True tells the serializer to expect a list of objects instead of a single object
    return Response(serializer.data)
  
  if request.method == 'POST':
    de_serializer = StateSerializer(data=request.data)
    if de_serializer.is_valid():
      de_serializer.save()
      return Response(de_serializer.data)
    else:
      return Response(de_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE']) 
def state_details(request, pk):
  if request.method == 'GET':
    state = State.objects.get(pk=pk)
    serializer = StateSerializer(state)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    state = State.objects.get(pk=pk)
    de_serializer = StateSerializer(state, data=request.data)
    if de_serializer.is_valid():
      de_serializer.save()
      return Response(de_serializer.data)
    else:
      return Response(de_serializer.errors)
  
  if request.method == 'DELETE':
    state = State.objects.get(pk=pk)
    state.delete()
    return Response(status=204)