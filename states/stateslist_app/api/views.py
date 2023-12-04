from rest_framework.response import Response
from stateslist_app.models import State
from stateslist_app.api.serializers import StateSerializer
from rest_framework.decorators import api_view


@api_view(['GET']) #GET is the default method, so you can leave it empty
def states_list(request):
  states = State.objects.all()
  serializer = StateSerializer(states, many=True) #many=True tells the serializer to expect a list of objects instead of a single object
  return Response(serializer.data)

@api_view() #GET is the default method, so you can leave it empty
def state_details(request, pk):
  state = State.objects.get(pk=pk)
  serializer = StateSerializer(state)
  return Response(serializer.data)