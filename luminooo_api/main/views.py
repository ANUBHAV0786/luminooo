from django.shortcuts import render

from rest_framework.views import APIView
from . serializer import TeacherSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from . import models

# Create your views here.
# class TeacherList(APIView):
#     def get(self, request):
#         teachers = models.Teacher.objects.all()        ## this issour  data
#         serializer = TeacherSerializer(teachers, many=True) ## we're serializing the data
#         return Response(serializer.data)

    # def post(self, request):
    #     serializer = TeacherSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)


class TeacherList(generics.ListCreateAPIView):   ## this type will handle list type record 
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]  ## added in STEP 7 this will make sure that only authenticated users can access the data

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):  ## this will handple the single record
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]  ## added in STEP 7 this will make sure that only authenticated users can access the data