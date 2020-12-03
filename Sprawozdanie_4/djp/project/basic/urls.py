from django.urls import path
from .views import case_list
urlpatterns = [
    path('case/', case_list),
]