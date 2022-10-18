from django.urls import path
from .views import informaions

app_name = "about"

urlpatterns = [path("", informaions, name="data")]
