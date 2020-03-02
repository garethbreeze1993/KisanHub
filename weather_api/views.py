from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from weather_api.models import Entry
from weather_api.serializers import EntrySerializer

@api_view(['GET', 'POST'])
def entry_list(request, format=None):
    
	if request.method == 'GET':
		entries = Entry.objects.all().order_by('date')
		serializer = EntrySerializer(entries, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = EntrySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Entries_List_Filtered(generics.ListAPIView):
    serializer_class = EntrySerializer
    
    def get_queryset(self):
        metric_type = self.kwargs.get('metric_type', None)
        location = self.kwargs.get('location', None)
        
        if metric_type is not None:
            return Entry.objects.filter(metric_type=metric_type).order_by('date')
        elif location is not None:
            return Entry.objects.filter(location=location).order_by('date')
        else:
            return Entry.objects.all().order_by('date')
        
        
        
        
        
        
        
        
        
        
        
 # Example of chaining on filter clauses       
#entries = Entry.objects.filter(metric_type=metric_type)
#return entries.filter(location=location)
