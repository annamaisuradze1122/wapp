from rest_framework import serializers
from .models import WorkoutDay, WorkoutGoal, WorkoutPlan, Exercise, ExerciseType


class WorkoutDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutDay
        fields = '__all__'


class WorkoutGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutGoal
        fields = '__all__'


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = ['name', 'workout_goals', 'workout_days', 'exercises']


class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    type = ExerciseTypeSerializer()
    
    class Meta:
        model = Exercise
        fields = '__all__'