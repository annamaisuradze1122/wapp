from django.contrib import admin
from .models import WorkoutDay, WorkoutGoal, WorkoutPlan, Exercise, ExerciseType

admin.site.register(WorkoutDay)
admin.site.register(WorkoutGoal)
admin.site.register(WorkoutPlan)
admin.site.register(ExerciseType)
admin.site.register(Exercise)

