from django.urls import path
from home.views import ReceipeAPI 

urlpatterns = [
    path('receipes/', ReceipeAPI.as_view()),
]