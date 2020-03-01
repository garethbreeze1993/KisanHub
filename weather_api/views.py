from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from weather_api.models import Entry
from weather_api.serializers import EntrySerializer

@api_view(['GET', 'POST'])
def entry_list(request, format=None):
    
	if request.method == 'GET':
		entries = Entry.objects.all()
		serializer = EntrySerializer(entries, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = EntrySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)