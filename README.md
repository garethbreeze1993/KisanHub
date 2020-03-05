
To run application 
Create Directory and do a git clone to get the necessary files 
Create a virtual environment and activate it 
Use command pip3 install -r requirements.txt to install dependencies 
Run python manage.py runserver to run application 
Go to localhost:8000/form and fill out the form to send get request to the JSON files.

To view all data sent to DRF API go to localhost:8000/api/entries, this is ordered by date.

To filter based on either location or metric type either type in 

localhost:8000/api/metric_type/{metric_type} to filter by metric type

localhost:8000/api/location/{location} to filter by location