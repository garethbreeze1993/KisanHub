from django.db import models

location_choices = (
('UK', 'UK'),
('England', 'England'),
('Wales', 'Wales'),
('Scotland', 'Scotland')

)

metric_choices = (
('Tmax', 'Tmax'),
('Tmin', 'Tmin'),
('Rainfall', 'Rainfall'),
)
'''
class Metric(models.Model):
	parameter = models.CharField(choices=metric_choices, max_length=128)
	value = models.SmallIntegerField()
'''
class Entry(models.Model):
	date = models.DateField() # change to positive integer field and change field to year.
	metric_type = models.CharField(choices=metric_choices, max_length=128)
	metric_value = models.SmallIntegerField()
	location = models.CharField(choices=location_choices, max_length=128)
	