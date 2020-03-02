from django.db import models
import datetime
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
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField() # need validation of some kind to check incorrect data not being passed in for month and year
    date = models.DateField(editable=False)
    metric_type = models.CharField(choices=metric_choices, max_length=128)
    metric_value = models.SmallIntegerField()
    location = models.CharField(choices=location_choices, max_length=128)
	
    def save(self, *args, **kwargs):
        self.date = datetime.date(self.year, self.month, 1)
        super().save(*args, **kwargs)
        
	
