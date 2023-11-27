from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# class StudentViewSet(viewsets.ModelViewSet):

#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
    

class StudentViewSet(APIView):

    def post(self,request):

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : 200,
                "msg" : "Data Added Successfully"
            })
        
    
    def get(self,request):

        obj = Student.objects.all()
        serializer = StudentSerializer(obj,many=True)

       
        return Response({
            "status" : 200,
            "msg" : "Data Fetch Successfully",
            "data" : serializer.data
        })