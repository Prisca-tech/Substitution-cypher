from django.shortcuts import render, redirect

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import LogEntry
from .serializers import LogEntrySerializer

@api_view(['GET', ])
class LogEntryListCreateView(generics.ListCreateAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

class LogEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer



   
