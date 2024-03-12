from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import WorkoutDay, WorkoutGoal, WorkoutPlan, Exercise, ExerciseType
from .serializers import WorkoutDaySerializer, WorkoutGoalSerializer, ExerciseTypeSerializer, WorkoutPlanSerializer,ExerciseSerializer
from rest_framework import permissions, decorators



@api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_workout_days(request):
    days = WorkoutDay.objects.all()
    serializer = WorkoutDaySerializer(days, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_exercise_types(request):
    types = ExerciseType.objects.all()
    serializer = ExerciseTypeSerializer(types, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_exercises(reuest):
    exercises = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_exercise(reuest, pk):
    exercises = Exercise.objects.get(id=pk)
    serializer = ExerciseSerializer(exercises, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_workout_goals(request):
    goals = WorkoutGoal.objects.all()
    serializer = WorkoutGoalSerializer(goals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_workout_plans(request):
    plans = WorkoutPlan.objects.all()
    serializer = WorkoutPlanSerializer(plans, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def create_workout_plan(request):
    serializer = WorkoutPlanSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@decorators.permission_classes([permissions.IsAuthenticated])
def workout_plan(request, pk):
    try:
        plan = WorkoutPlan.objects.get(id=pk)
    except WorkoutPlan.DoesNotExist:
        context = {
            'message': 'Plan was not found.'
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WorkoutPlanSerializer(plan)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = WorkoutPlanSerializer(plan, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    