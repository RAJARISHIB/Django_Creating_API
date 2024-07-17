from django.shortcuts import render
from .models import course
from .serializers import Courseserializers
from rest_framework import viewsets
# Create your views here.

class Courseviews(viewsets.ModelViewSet):
    queryset = course.objects.all()
    serializer_class = Courseserializers