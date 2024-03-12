# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import WorkoutPlanSerializer, ExerciseTypeSerializer, ExerciseSerializer
# from account.models import WorkoutPlan, ExerciseType, Exercise
# from account.forms import WorkoutPlanForm


# @api_view(['GET'])
# def get_plans(request):
#     item = WorkoutPlan.objects.all()
#     serializer = WorkoutPlanSerializer(item, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_plan(request, pk):
#     item = WorkoutPlan.objects.get(id=pk)
#     serializer = WorkoutPlanSerializer(item, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def update_plan(request, pk):
#     plan = WorkoutPlan.objects.get(id=pk)
#     serializer = WorkoutPlanSerializer(plan, data=request.data, many=False)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)



# @api_view(['GET'])
# def get_exercise_types(request):
#     item = ExerciseType.objects.all()
#     serializer = ExerciseTypeSerializer(item, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_exercise_type(request, pk):
#     item = ExerciseType.objects.get(id=pk)
#     serializer = ExerciseTypeSerializer(item, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_exercises(request):
#     item = Exercise.objects.all()
#     serializer = ExerciseSerializer(item, many=False)
#     return Response(serializer.data)