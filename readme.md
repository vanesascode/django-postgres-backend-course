# Django, Django Rest Framework & postgres course

Note on installation:

It's recommended to use only one package manager (`pip or pip3`) consistently within a project, depending on the specific Python version you are targeting.

If you are working on a Python 2 project, use pip to install packages. If you are working on a Python 3 project, use pip3 to install packages. This way, you ensure that the correct packages are installed for the intended Python version.

## 🌟 VIRTUAL ENVIRONMENT:

Create environment:

`python -m venv <name of environment>`

Activate the environment:

`<name of environment>\Scripts\activate` (it has to be in the root folder)

You'll see this:

`(<name of environment>) PS C:\Users...etc.`

Now, all the commands you run will be only be in the environment.

See all you have installed in the environment:

`pip freeze`

To deactivate environment:

`<name of environment>\Scripts\deactivate`

## 🌟 DJANGO:

[Installation](https://www.djangoproject.com/download/)

Creation of project:
`django-admin startproject <name of project>`

Then, you get inside your project `cd <name of project`>

### 🔹 APPS inside Django

`python manage.py startapp <name of project_app>`

Add your app. Go to the folder with the name of your project alone, and inside, in `settings.py`, add your app:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<name of project_app>',
]
```

![image](https://github.com/vanesascode/typescript-microsoft-course-build-javascript-applications-using-typescript/assets/131259155/2bd68570-a984-4777-b08a-d415f45c9867)

### 🔹 RUN the server

`python manage.py runserver`

Copy the address (ex. http://127.0.0.1:8000/) and open it in the browser.

### 🔹 RUN the migrations

`python manage.py migrate`

### 🔹 CREATE superuser

`python manage.py createsuperuser`

Enter username, email and password.

Enter in the browser: http://127.0.0.1:8000/admin

![image](https://github.com/vanesascode/typescript-microsoft-course-build-javascript-applications-using-typescript/assets/131259155/345f7f37-877a-400c-a0bd-83cade2e2904)

### 🔹 CREATE model, table

Create a file named `urls.py` in the `<name of project_app>`

### 🔹 CREATE a schema in the models.py file

For example, this one is called State (Inmueble)

```
class State(models.Model):
  address = models.CharField(max_length=250)
  city = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  image = models.CharField(max_length=900)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.address
```

The `__str__` method in the States class is to define how an instance of the States class should be represented as a string.

For example, if you have an instance of the States class called state with the address attribute set to "123 Main St", calling `str(state)` or `print(state)` will return "123 Main St".

### 🔹 Register the schema in the admin.py file

Import the schema in the admin.py file:
`from <name of project_app>.models import State`

Then register:
`admin.site.register(State)`

### 🔹 Reflect the changes in the django admin: MIGRATION

We pass the data in models.py to SQL syntax, that represents the result of a table.

In the console (inside the `<name of project>` folder, remember, `cd <name of project>`):
`python manage.py makemigrations`

Now we have the code to execute the migration.

Now execute the migration:
`python manage.py migrate`

❗ If you made mistakes and have to start again: Delete all files in migrations folder (except for `__init__.py`) + run commands `rm db.sqlite3` + `python manage.py makemigrations` + `python manage.py migrate` - Remeber, you always must drop the database table too. And you'll have to create a super admin again: `python manage.py createsuperuser`.

👉 `db.sqlite3` is the default database file that Django creates when you first initialize a Django project. It is a SQLite database file that Django uses to store data for your application. SQLite is a lightweight and self-contained database engine that is included with Python, making it a convenient choice for development and testing purposes. The db.sqlite3 file will be located in the same directory as your Django project's manage.py file.

### 🔹 Add the principal url of your app inside the project:

In your `<name of project>` folder, there's a `urls.py` file, in there, import `include` and add your url:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('<name of project>/', include('<name of project_app>.urls')),
]
```

### 🔹 Add the urls and defs of your app to make requests possible:

In your `<name of project_app>` folder, create a `urls.py` file. In there, add the path that represents the request to get the list of whatever is your table about.

```
from django.urls import path
from <name of project_app>.views import <name of table>_list

urlpatterns = [
  path('list/', <name of project_app>, name='<name of project>-list'),
]
```

The `<name of table>_list` we import, is a function that first we have to create in our `views.py` file.

![image](https://github.com/vanesascode/fils/assets/131259155/6b3a0d01-c6bd-47e9-898a-f07b5abc00a0)

Imagine you have a project called "states" and inside, an app called "stateslist_app", and you created a model called "State" (put it in singular, cos it will add a final "s") inside the app. Then, in your app you created the path "states/" and then, inside your app, the path "list/". See what it is like then, in the app's `views.py` file:

```
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
```

## 🌟 Django Rest Framework

Django REST Framework is a powerful and flexible toolkit for building Web APIs in Django. It provides a set of tools and libraries for easily building and interacting with RESTful APIs. With Django REST Framework, you can quickly build APIs that support CRUD operations (Create, Retrieve, Update, Delete) and handle authentication, serialization, pagination, and more. It is widely used in Django projects for creating robust and scalable APIs.

INSTALLATION:

- Activate the environment:

`<name of environment>\Scripts\activate` (it has to be in the root folder)

- Go to your project's folder in the command line:

`cd <name of project>`

- Run the commands from the [DOCS](https://www.django-rest-framework.org/#installation)

`pip install djangorestframework`

- Add it to the list of installed apps in the `settings.py` file in the project's folder:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'states_app',
    'rest_framework',
]
```

![image](https://github.com/vanesascode/fils/assets/131259155/2a942757-d8d4-4a64-83d6-0925262b900e)

SERIALIZATION:

![image](https://github.com/vanesascode/fils/assets/131259155/ea8b9c06-e183-4fb8-8b2e-421f3a850869)

DE-SERIALIZATION:

![image](https://github.com/vanesascode/fils/assets/131259155/5a65ed37-7de3-4503-af94-096b3b0f2538)

### 🔹 Build Web API

Go to your project's app (in my case it is `stateslist_app`)

Create a folder called `api`. In this folder you create the structure that gives support to the VIEWS, URLS and SERIALIZERS.

Inside the `api` folder create a file `urls.py`, a file `views.py` and a file `serializers.py`

In the `urls.py` file you can copy what you have in the other `urls.py` file we have, but importing the functions from the `views.py` file inside the api:

```
from django.urls import path
from stateslist_app.api.views import states_list, state_details

urlpatterns = [
  path('list/', states_list, name='states-list'),
  path('<int:pk>/', state_details, name='state-details'),
]
```

👉👉👉 In fact, we don't need the `urls.py` and the file `views.py` at the level of your project's app. We will just use the ones inside the `api` folder.

In the file `serializers.py` we create the searializer class that will defines the fields that will be serialized and deserialized when interacting with instances of the 'State' model:

```
from rest_framework import serializers

class StateSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  address = serializers.CharField()
  city = serializers.CharField()
  description = serializers.CharField()
  image = serializers.CharField()
  active = serializers.BooleanField()
```

Now, we can use this class in the functions of the `views.py` file:

```
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
def state_detail(request, pk):
  state = State.objects.get(pk=pk)
  serializer = StateSerializer(state)
  return Response(serializer.data)
```

Now we have to go back to the `urls.py` file of our project (in my case, `states`), and you have to change the path with `api`:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('states/', include('stateslist_app.api.urls')),
]
```

Now you can run the server, and will see the data much better thanks to Django Rest Framework:

![image](https://github.com/vanesascode/fils/assets/131259155/f9bf4e5b-b794-4e1e-887a-6897dbdde7d9)

### 🔹 Add POST view function & create method in the serializer class

```
@api_view(['GET', 'POST']) #GET is the default method, so you can leave it empty
def states_list(request):
  if request.method == 'GET':
    states = State.objects.all()
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)

  if request.method == 'POST':
    de_serializer = StateSerializer(data=request.data)
    if de_serializer.is_valid():
      de_serializer.save()
      return Response(de_serializer.data)
    else:
      return Response(de_serializer.errors)
```

The `de_serializer` instance is responsible for deserializing the data received in the request (request.data). Deserialization is the process of converting the raw data into a Python object that can be easily manipulated and validated.

`is_valid()` is a method provided by the Django REST Framework's serializer

```
from rest_framework import serializers
from stateslist_app.models import State

class StateSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  address = serializers.CharField()
  city = serializers.CharField()
  description = serializers.CharField()
  image = serializers.CharField()
  active = serializers.BooleanField()

  def create(self, validated_data):
    return State.objects.create(**validated_data)
```

The `self` parameter allows you to access the instance variables and other instance methods within the class.

The double asterisks `**` is used to unpack a dictionary into keyword arguments when calling a function or method. In this case, it allows passing the values from the validated_data dictionary as individual keyword arguments to the create method.

Now you can post a new instace to the table State:

![image](https://github.com/vanesascode/fils/assets/131259155/4ac14a07-0862-43f1-b5eb-37d4f652596d)

### 🔹 From a functions model to a class model: CLASS APIVIEW

Django's APIView class is a `base class` that provides a convenient way to `create API views`. It is designed to be used with Django's built-in rest_framework module for building RESTful APIs.

```
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    def get(self, request):
        # Handle GET request logic here
        return Response("GET request processed")

    def post(self, request):
        # Handle POST request logic here
        return Response("POST request processed")
```

The APIView class also provides some built-in functionalities such as request parsing, response formatting, authentication, permission handling, and more. It allows you to easily `handle common API tasks without having to write repetitive code.`

### 🔹 Entity Validations

`Serializer Validation`: In Django Rest Framework, serializers provide a validate\_<fieldname>() method that can be used to perform field-specific validation when deserializing input data.

We set them in the `serializers.py` file inside the app, and inside the api folder.

First, you create a function that will have the condition:

```
def column_length(value):
  if len(value) < 2:
    raise serializers.ValidationError('Address is too short')
```

And then you apply it to the specific property you want:

```
address = serializers.CharField(validators=[column_length])
```

### 🔹 Core Arguments

In Django REST Framework, the "core arguments" in serializer fields are the arguments that are commonly used to `configure and customize the behavior of serializer fields`. Some of the core arguments include:

- `read_only`: Specifies whether the field is read-only or not.

- write_only: Specifies whether the field is write-only or not.

- `required`: Specifies whether the field is required or not during deserialization.

- allow_null: Specifies whether the field allows null values or not.

- default: Specifies the default value for the field if no value is provided.

- `validators`: Specifies a list of validators to apply to the field.

- source: Specifies the name of the attribute or method on the model that the field should be serialized from or deserialized into.

These core arguments are used to define the behavior of serializer fields and customize how data is serialized and deserialized.

### 🔹 Inheriting from ModelSerializer VS inheriting from Serializer

The main difference is that the first approach (ModelSerializer) automatically generates the serializer fields based on the model, while the second approach (Serializer) requires you to define each field manually.

```
class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields = '__all__'

```

This code snippet above defines a serializer class StateSerializer that inherits from ModelSerializer. It is used to serialize and deserialize instances of the State model. The Meta class inside StateSerializer specifies that the serializer should be based on the State model and include all fields (fields = '**all**').

In Python, the `Meta class` is a way to define `metadata for a class`.

In case you don't want all fields to be seen, you can say which ones you want, with either `fields` or `exclude`:

```
class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    # fields = '__all__'
    # fields = ['id', 'address', 'description', 'active']
    exclude = ['id']

```

Now see:

```
class StateSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  address = serializers.CharField(validators=[column_length])
  city = serializers.CharField(validators=[column_length])
  description = serializers.CharField()
  image = serializers.CharField()
  active = serializers.BooleanField()
```

This second code snippet defines a serializer class StateSerializer that inherits from Serializer. This type of serializer requires you to manually define each field and its validation rules.

## 🌟 API Documentation - [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html#usage)

DRF-YASG is a Python library that integrates with Django REST Framework (DRF) to generate `OpenAPI (formerly known as Swagger) documentation for your RESTful APIs`. It provides a set of decorators and classes that allow you to annotate your DRF views and serializers with OpenAPI metadata, which is then used to generate interactive API documentation.

DRF-YASG stands for `Django REST Framework Yet Another Swagger Generator`. It aims to simplify the process of documenting your APIs by automatically generating the OpenAPI schema and providing a user-friendly interface to `explore and test your API endpoints`.

Apart from installing: `pip install drf-yasg`

You also need to install `pip install setuptools`

Now our urls file in the project states remains like this:

```
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="States",
      default_version='v1',
      description="Sates documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vanesascode@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('states/', include('stateslist_app.api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

```

`http://127.0.0.1:8000/swagger/`

---

# 🌟 SUMMARY SO FAR - To build a new API and update the database:

### build a new API

- Create the model (inside migrations folder)

- Create the serializer class (inside the api folder)

- Create the views classes (inside the api folder)

- Add the path in the urls file (inside the api folder)

- Add the model to the admin file so you can manage it in the admin interface (inside the app folder, example: `stateslist_app`)

### update the database

- Eliminate the current database file ( example: `db.sqlite3`)

- Get inside the environment (in the root folder, example: `PS C:\Users\Vanesa\django-postgres-backend-course\`, run the command `menv\Scripts\activate`), and go to the level of the project folder (not the app folder, example: `(menv) PS C:\Users\Vanesa\django-postgres-backend-course\states>`)

- There, run the command: `python manage.py makemigrations`

- If you are asked (did you rename the xxxxxx model to xxxxxx ? ) If you say NO, then it will create from scratch, which is better. You may be asked other questions

- Then, run the command `python manage.py migrate`

- Then, we create the use again. Run `python manage.py createsuperuser` and fill in the filds (remember, you won't see the password, but it is being introduced!!!)

- You can run the server: `python manage.py runserver`. And go to the admin panel: http://127.0.0.1:8000/admin

👉 `makemigrations` is used to generate migration files based on your model changes, while `migrate` applies those migrations to update the database schema.

---

❗ If there are many errors and can't start sever: Delete all files in migrations folder (except for `__init__.py`) + run commands `rm db.sqlite3` + `python manage.py makemigrations` + `python manage.py migrate` - Remember, you always must drop the database table too. And you'll have to create a super admin again: `python manage.py createsuperuser`.

---

## 🌟 Relations between models

A relational database is a type of database that:

- `organizes data into tables with rows and columns`. (In mongoDB we talk about collections and documents)

- `It uses a structured query language (SQL)` to manage and manipulate the data. (MongoDB uses its own query language MQL)

- `Tables are related to each other through common fields`, allowing for efficient data retrieval and manipulation. (In MongoDB, collections are not directly related to each other through common fields like tables in a relational database. Instead, MongoDB provides a feature called "references" or "embedded documents" to establish relationships between collections.)

![image](https://github.com/vanesascode/django-postgres-backend-course/assets/131259155/d5ba6919-d125-40a9-8513-5ba879a7be98)

![image](https://github.com/vanesascode/django-postgres-backend-course/assets/131259155/f66f9f44-a5c9-4829-a989-b64a392369e9)

![image](https://github.com/vanesascode/django-postgres-backend-course/assets/131259155/9c408ce4-d3ed-47e5-b316-2486420a19cc)

Example of one to many:

```
class Business(models.Model):
  name = models.CharField(max_length=250)
  website = models.URLField(max_length=250)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name

class State(models.Model):
  address = models.CharField(max_length=250)
  city = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  image = models.CharField(max_length=900)
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='stateslist')


  def __str__(self):
    return self.address

```

After any change you do to your models, remember: `python manage.py makemigrations` + `python manage.py migrate`

For now, when we check our states list, we only see the id of the business that is related. And in the business list, I don't know what states each have. So:

### 🔹 Nested results between models

We can add the list of states in the business model:

```
class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
  stateslist = StateSerializer(many=True, read_only=True)
  class Meta:
    model = Business
    fields = '__all__'
```

(stateslist is the related_name in the state model)

![image](https://github.com/vanesascode/django-postgres-backend-course/assets/131259155/6d528c5d-274e-4ea4-9c24-f5cb3634fd9c)

But what if you don't want it to return the whole state object, only some fields:

We can return only what is in the **str** funcion in the models.

So in our business class:

```
class BusinessSerializer(serializers.ModelSerializer):
  stateslist = serializers.StringRelatedField(many=True)
  class Meta:
    model = Business
    fields = '__all__'
```

And in the State model:

```
class State(models.Model):
  address = models.CharField(max_length=250)
  city = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  image = models.CharField(max_length=900)
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='stateslist')

  def __str__(self):
    return self.address
```

So, only we'll get the address.

A especific way of only returning the ids:

```
stateslist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
```

We can also return the URL where you find the state object in the admin interface:

```
 stateslist =  serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='state-details' # this is the name we used in the path of the urlpatterns, to get one onlystate
    )
```

Also, we need to add the request to the view class, in the get method:

```
class BusinessListApiView(APIView):
  def get(self, request):
    businesses = Business.objects.all()
    serializer = BusinessSerializer(businesses, many=True, context={'request': request})
    return Response(serializer.data)
```

And you have it:

![image](https://github.com/vanesascode/django-postgres-backend-course/assets/131259155/006ece6d-5f4d-47fc-a277-56685eb8df28)

### 🔹 Instead of Primary Key, use a Unique URL

Using HyperlinkedModelSerializer:

```
class BusinessSerializer(serializers.HyperlinkedModelSerializer):
  stateslist = StateSerializer(many=True, read_only=True)

  class Meta:
    model = Business
    fields = '__all__'
```

![image](https://github.com/vanesascode/django-postgres-backend-course/assets/131259155/fba179a7-b906-4593-9414-8c654690d017)
