from django.urls import path
from .views import (
    get_workout_days,
    get_exercise_types,
    get_exercises,
    get_workout_goals,
    get_workout_plans,
    get_exercise,
    create_workout_plan,
    workout_plan
)


urlpatterns = [
    path('days/', get_workout_days,  name='workout_days'),
    path('exercise_types/', get_exercise_types,  name='get_exercise_types'),
    path('exercises/', get_exercises,  name='get_exercises'),
    path('exercises/<str:pk>', get_exercise,  name='get_exercise'),
    path('goals/', get_workout_goals,  name='get_workout_goals'),
    path('plans/', get_workout_plans,  name='get_workout_plan'),
    path('plans/', create_workout_plan,  name='create_workout_plan'),
    path('plans/<str:pk>', workout_plan,  name='update_workout_plan')
]
