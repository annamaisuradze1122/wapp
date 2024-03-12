# from rest_framework import serializers
# from account.models import WorkoutPlan, Exercise, ExerciseType


# class ExerciseTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExerciseType
#         fields = '__all__'


# class ExerciseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Exercise
#         fields = '__all__'


# class WorkoutPlanSerializer(serializers.ModelSerializer):
#     exercise_type = ExerciseTypeSerializer(many=False)

#     class Meta:
#         model = WorkoutPlan
#         fields = '__all__'
        