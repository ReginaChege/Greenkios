from django.shortcuts import render
from rest_framework.views import Response
from rest_framework import status

# Create your views here
from .serializers import CustomerSerializer
from rest_framework.views import APIView
from customer.models import Customer

class CustomerListView(APIView):
    def get (self,request):
        customer=Customer.objects.all()
        serializer=CustomerSerializer(customer ,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_created)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):
    def get(self,request,id, format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer,request.data)
    
    def put(self , request , id , format = None):
        customer = Customer.objects.get(id = id)
        serializer = CustomerSerializer (customer, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        customer=customer.objects.get(id=id)  
        customer.delete()    
        return Response("customer deleted",status=status.HTTP_204_NO_CONTENT_DELETE_) 
           
        
