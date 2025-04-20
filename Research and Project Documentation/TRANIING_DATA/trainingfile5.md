https://www.youtube.com/watch?v=E-MqY180IOM&list=PLgnySyq8qZmox-EAyxkPYe14ZVCVSBMdK&index=90

this is the video link for this file or STEP 5

we will create REST API for our project
        for this we need to 
            1. install django REST Framework
                 use # pip install djangorestframework

            2. Now add rest framework inside the settings.py in Installed_Apps section 
                Now our Installed_apps sections in settings.py look like below


                    INSTALLED_APPS = [
                                    'main',
                                    'rest_framework'
                                    'django.contrib.admin',
                                    'django.contrib.auth',
                                    'django.contrib.contenttypes',
                                    'django.contrib.sessions',
                                    'django.contrib.messages',
                                    'django.contrib.staticfiles',
                                ]

                        We're using React for frontend, and our API response will be JSON format

                        So, to convert model data to json we will use Serializer 

                        So, we need to create Serializer 


See if we are creating website we will use forms and if we are creating API then we will create Serializer

So we create Serializer as per our model and we use models to create the serializer.
Serializers in Django REST Framework are responsible for converting model instances to a format that can be easily rendered into JSON, XML, or other content types. They also handle the reverse process, deserializing data back into model instances after validating it.


So create a file called serializer.py inside the main folder

            from rest_framework import serializers
            from .import models


            class TeacherSerializer(serializers.ModelSerializer):
                class Meta:
                    model = models.Teacher
                    fields = '__all__'
                    # fields = ['full_name', 'date_of_birth', 'email', 'password', 'qualification', 'mobile_number', 'address', 'subject']


now we have defined serializer now we need to do 2 things 
    1.how to see response 
    2.how to see serializer response 

Now open our 1.views.py file and use class based view.
and 2.We will import API view from rest_framework 
        from rest_framework import APIView
        from . serializer import TeacherSerializer
        from . import models


    3.We also need to bind that view to the URL 
            we need to first create urls.py file in our main folder

            from django.urls import path
            from . import views


            urlpatterns = [
                path('teacher/',views.TeacherList.as_view())

        Now we need to add this urls.py(anubhav created) of main folder into our urls.py of luminooo_api folder (self created by django framework)

        Refer this image to clearity step5addurls.pytourls.py.png inside images for training


        NOw once all done start the server by # py manage.py runserver

        now go to http://127.0.0.1:8000/api/teacher/ here we will find our TEacher api RESPONSE 

                here you will get 200 status code


        Now add data in Teacher table schema and then refresh the /api/teacher page and check you have get the data you have entered.


=============================================================================
=============================================================================

                    LEARNING LEARNING LEARNING                              

=============================================================================
=============================================================================



Ah, a fundamental choice when building views in Django! Let's explore both Class-Based Views (CBVs) and Function-Based Views (FBVs), highlighting their characteristics and when you might choose one over the other.

Function-Based Views (FBVs)

As the name suggests, Function-Based Views are Python functions that take an HttpRequest object as their first argument and return an HttpResponse object. They are the more traditional way of writing views in Django and are often simpler for basic tasks.

Structure of an FBV:

Python

from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    if request.method == 'GET':
        # Handle GET request (e.g., display a form, list data)
        data = {'message': 'Hello from a function-based view!'}
        return render(request, 'my_template.html', data)
    elif request.method == 'POST':
        # Handle POST request (e.g., process form submission)
        form_data = request.POST
        # ... process the data ...
        return HttpResponse('Data submitted successfully!')
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
Key Characteristics of FBVs:

Explicit Request Handling: You explicitly check the request.method (e.g., 'GET', 'POST') within the function using conditional statements (if/elif/else) to determine how to process the incoming request.
Clear Control Flow: The logic for handling different HTTP methods is clearly laid out within the function.
Simplicity for Basic Tasks: For straightforward views that perform a single action or handle a limited number of HTTP methods, FBVs can be concise and easy to understand.
Easier to Follow for Beginners: The linear flow of execution in a function can be more intuitive for developers new to Django.
When to Consider FBVs:

For very simple views that perform a single action and don't require much complex logic or handling of multiple HTTP methods.
When you need fine-grained control over the request-response cycle.
When you prefer the explicit nature of handling different HTTP methods within conditional statements.
Class-Based Views (CBVs)

Class-Based Views are Python classes that inherit from base view classes provided by Django's views module. They offer a more organized and reusable way to handle common view patterns.

Structure of a Basic CBV (using View):

Python

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

class MyView(View):
    def get(self, request):
        data = {'message': 'Hello from a class-based view!'}
        return render(request, 'my_template.html', data)

    def post(self, request):
        form_data = request.POST
        # ... process the data ...
        return HttpResponse('Data submitted successfully via POST!')

    def put(self, request):
        # Handle PUT request
        return HttpResponse("Data updated via PUT!")

    def delete(self, request):
        # Handle DELETE request
        return HttpResponse("Data deleted!")
Key Characteristics of CBVs:

Implicit Request Handling: CBVs use methods that correspond to HTTP methods (e.g., get(), post(), put(), delete()). Django's framework automatically dispatches the incoming request to the appropriate method based on the request.method.
Code Reusability and Organization: CBVs promote code reuse through inheritance. Django provides generic CBVs (like ListView, DetailView, FormView, CreateView, UpdateView, DeleteView) that handle common web development tasks, reducing the amount of code you need to write.   
Mixins for Adding Functionality: CBVs can easily incorporate mixins, which are classes that provide reusable functionality that can be "mixed in" with your view class. This allows you to add features like authentication, permission checking, and pagination with minimal code.   
Better Structure for Complex Views: For views that handle multiple HTTP methods or involve more intricate logic, CBVs can provide a more organized and maintainable structure.
Increased Readability for Complex Logic: Separating the handling of different HTTP methods into distinct methods can improve the readability of more complex view logic.
Common Generic Class-Based Views:

Django provides a set of powerful generic CBVs that handle many common web development patterns:   

TemplateView: Simply renders a template.   
ListView: Displays a list of objects.
DetailView: Displays the details of a single object.   
FormView: Handles the display and processing of a form.   
CreateView: Handles the creation of new objects using a form.   
UpdateView: Handles the editing of existing objects using a form.
DeleteView: Handles the deletion of objects.   
Example using a Generic CBV (ListView):

Python

from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # Optional: specify a custom template
    context_object_name = 'products'  # Optional: change the name of the object list in the template
When to Consider CBVs:

When you need to handle multiple HTTP methods for a single resource.
When you want to leverage Django's built-in generic views for common tasks like displaying lists, details, forms, etc.
When you want to improve code reusability and maintainability, especially for more complex views.
When you want to utilize mixins to easily add functionality to your views.
For larger and more complex applications where organization and reusability become increasingly important.
In essence:

FBVs are straightforward and often suitable for simple tasks where explicit request handling is desired.   
CBVs offer a more structured and reusable approach, especially beneficial for handling multiple HTTP methods and leveraging Django's generic views and mixins for common web development patterns.   
The choice between FBVs and CBVs often comes down to the complexity of the view and your preference for code organization and reusability. Many Django projects use a mix of both, choosing the most appropriate approach for each specific view. As your applications grow in complexity, you'll likely find yourself leaning more towards the power and organization offered by Class-Based Views.