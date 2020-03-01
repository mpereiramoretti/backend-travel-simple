from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Host
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
    elif request.method == 'OPTIONS':
        hosts = Host.objects.all()
        serializer = HostSerializer(hosts, context ={'request': request}, many = True)

        return Response({
            'data': serializer.data
        })
