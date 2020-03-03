from django.forms import ModelForm
from weather_api.models import Entry

class EntryForm(ModelForm):
	model = Entry
	fields = ('metric_type', 'location')
	

