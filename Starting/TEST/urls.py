from django.urls import path
from . import views
app_name = "names"
urlpatterns = [
	path("",views.index , name="index"),
	path("name/",views.name, name="name")
	
]