from django.urls import path
from stateslist_app.api.views import states_list, state_details

urlpatterns = [
  path('list/', states_list, name='states-list'),
  path('<int:pk>/', state_details, name='state-details'),
]