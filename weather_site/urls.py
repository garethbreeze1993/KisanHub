"""weather_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weather_api.views import entry_list, Entries_List_Filtered, get_data_for_api

urlpatterns = [
    path('admin/', admin.site.urls),
	path('api/entries/', entry_list),
	path('api/entries/metric_type/<str:metric_type>/', Entries_List_Filtered.as_view()),
	path('api/entries/location/<str:location>/', Entries_List_Filtered.as_view()),
	path('form/', get_data_for_api),
]
