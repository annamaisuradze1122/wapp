# """
# URL configuration for wapp project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views

# """
# from django.urls import path
# from .views import get_plan, get_plans, get_exercise_types, get_exercise_type, get_exercises, update_plan


# urlpatterns = [
#     path('plans/', get_plans,  name='workout_plans'),
#     path('plans/<str:pk>/', get_plan,  name='workout_plan'),
#     path('plans/<str:pk>/update', update_plan,  name='update_workout_plan'),
#     path('exercise_types/', get_exercise_types,  name='get_exercise_types'),
#     path('exercise_types/<str:pk>/', get_exercise_type,  name='get_exercise_type'),
#     path('exercises/', get_exercises,  name='get_exercises'),
# ]
