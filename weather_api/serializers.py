import datetime
from django.utils import timezone
from rest_framework import serializers
from weather_api.models import location_choices, metric_choices, Entry

'''
class MetricSerializer(serializers.ModelSerializer):
	#parameter = seraializers.ChoiceField(choices=metric_choices)
	#value = seraializers.IntegerField()
	class Meta:
		model = Metric
		fields = ('id', 'parameter', 'value')
'''		
class EntrySerializer(serializers.ModelSerializer):
	#metric_type = MetricSerializer()
	#location = seraializers.ChoiceField(choices=location_choices)
	class Meta:
		model = Entry
		fields = ('id', 'metric_type', 'location', 'year', 'month', 'metric_value')
		
	
