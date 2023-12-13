from django.urls import path
# from stateslist_app.api.views import states_list, state_details
from stateslist_app.api.views import StateListApiView, StateDetailApiView


# OPTION WITH CLASS APIView:

urlpatterns = [
  path('list/', StateListApiView.as_view(), name='states-list'),
  path('<int:pk>/', StateDetailApiView.as_view(), name='state-details'),
]

# OPTION WITH DECORATORS:

# urlpatterns = [
#   path('list/', states_list, name='states-list'),
#   path('<int:pk>/', state_details, name='state-details'),
# ]



# The urls.py file is responsible for mapping URLs to views. It defines the URL patterns for your application. The views.py file contains the views, which are Python functions or classes that handle HTTP requests and return HTTP responses. The urls.py file references the views defined in views.py to determine which view should be called when a particular URL is requested.