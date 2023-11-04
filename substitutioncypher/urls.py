from django import views
from django.contrib import admin
from django.urls import path, include
from .views import LogEntryListCreateView
from .views import LogEntryDetailView
from .views import *
from . import views



urlpatterns = [
    path('LogEntry', views.LogEntry, name='log-entry'),
    path('log-entries/', views.LogEntryListCreateView, name='log-entry-create'),
    path('log-entries/list/', views.LogEntryDetailView.as_view(), name='log-entry-list'),
]


