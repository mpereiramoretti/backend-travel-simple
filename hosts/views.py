from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Host, Bedroom
from .serializers import *
from django.shortcuts import render

# Create your views here.
@api_view(['GET', 'POST'])
def hosts_list(request):
    if request.method == 'GET':
        hosts = Host.objects.all()
        serializer = HostSerializer(hosts, context ={'request': request}, many = True)

        return Response({
            'data': serializer.data
        })
    elif request.method == 'POST':
        serializer = HostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def host_detail(request, host_pk):
  #Retrieve, update or delete a host by id/pk.
    try:
        host = Host.objects.get(pk = host_pk)
    except Host.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = HostSerializer(host, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HostSerializer(host, data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        host.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def bedroom_list_by_host(request, host_pk):
    if request.method == 'GET':
        bedrooms = Bedroom.objects.filter(host = host_pk)
        serializer = BedroomSerializer(bedrooms, context ={'request': request}, many = True)

        return Response({
            'data': serializer.data
        })
    elif request.method == 'POST':
        serializer = BedroomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bedroom_detail(request, host_pk, bedroom_pk):
  #Retrieve, update or delete a host by id/pk.
    try:
        bedroom = Bedroom.objects.get(pk = bedroom_pk)
    except Host.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BedroomSerializer(bedroom, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BedroomSerializer(bedroom, data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        bedroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
