from django.shortcuts import render
from stateslist_app.models import State
from django.http import JsonResponse

# Create your views here.

def states_list(request):
  states = State.objects.all() #retrieves all objects from the State model and assigns them to the states variable.
  data = {
    'states': list(states.values()) #creates a dictionary called data with a key called states and sets its value to a list of the values from the states variable.
  }
   
  return JsonResponse(data) #returns the data dictionary as a JSON response to the client

  
def state_details(request, pk):
  state = State.objects.get(pk=pk) #retrieves the state object with the specified primary key (pk) from the State model and assigns it to the state variable.
  data = {
      'address': state.address,
      'city': state.city,
      'description': state.description,
      'image': state.image
    }
  
  return JsonResponse(data)