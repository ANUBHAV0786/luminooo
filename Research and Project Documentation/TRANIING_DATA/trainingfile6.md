https://www.youtube.com/watch?v=aly_D7CL7CQ&t=9s

In this we learn how to POST, UPDATE, DELETE the datavia REST Frmework

In step 5 we used API view to define our get and post methods , and 

NOw we will first convert our API view to GENERIC view

use Django tutorial 
==============================================================================================
STEP 6 
==============================================================================================
NOW change your main/views file to ::
from django.shortcuts import render

from rest_framework.views import APIView
from . serializer import TeacherSerializer
from rest_framework.response import Response
from rest_framework import generics
from . import models



class TeacherList(generics.ListCreateAPIView):   ## this type will handle list type record 
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):  ## this will handple the single record
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer

==============================================================================================

step 6.b  Change the main/urls.py file to this below 

from django.urls import path
from . import views


urlpatterns = [
    path('teacher/',views.TeacherList.as_view()),
    path('teacher/<int:pk>/',views.TeacherDetail.as_view()),

]

================================================================================================
After doing 6.a and 6.b 

we will go to localhost:8000/api/teacher

Here we will get --->>>> step6apiresponseformimage.png


Here  we have multiple things 
        1. We can do GET the data and then we also got 2 type of GET response in API keys and in JSON
        2. We get the OPTION  header which will give and define what options we have and we can put it in our data , it like defining the schema of the teacher 
        3. we also get the POST option in the RAW data and as well as in the HTML form.
================================================================================================
step 6.c 
Now at 127.0.0.1:8000/api/teacher/ we will FIll our HTML form and check whether the data is propagated or NOT.
         