from django.urls import path
from . import views
urlpatterns = [
	path("",views.index , name="index"),
	# path("<str:name>",views.greet, name="greet"),
	path("h1",views.seperate, name="seperate"),
	path("h3.css",views.hay, name="css")

]