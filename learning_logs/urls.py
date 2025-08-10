"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),
    # Show a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
    # Delete operations
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),

    # Show the search results
    path('search/', views.search_results, name='search_results'),
]

