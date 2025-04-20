from django.shortcuts import render

from rest_framework.views import APIView
from . serializer import TeacherSerializer
from rest_framework.response import Response
from . import models

# Create your views here.
class TeacherList(APIView):
    def get(self, request):
        teachers = models.Teacher.objects.all()        ## this issour  data
        serializer = TeacherSerializer(teachers, many=True) ## we're serializing the data
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = TeacherSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)