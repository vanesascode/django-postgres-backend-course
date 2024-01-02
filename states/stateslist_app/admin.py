from django.contrib import admin
from stateslist_app.models import State, Business, Comment

# Register your models here.
admin.site.register(State)
admin.site.register(Business)
admin.site.register(Comment)