from django.urls import path
from .views import Index,JSON

urlpatterns = [
    path("",Index ,name="Home"),
    path("JSON/", JSON, name = "Json_data"),
]
