from django.db import models
import uuid


class WorkoutDay(models.Model):
    DAYS = (
        ('sunday', 'SUNDAY', ),
        ('monday', 'MONDAY', ),
        ('tuesday','TUESDAY'),
        ('wednesday','WEDNESDAY'),
        ('thursday', 'THURSDAY'),
        ('friday', 'FRIDAY'),
        ('saturday','SATURDAY'),
    )
    day = models.CharField(choices=DAYS, max_length=30)

    class Meta:
        db_table = 'workout_days'

    def __str__(self):
        return self.day
    

class ExerciseType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = 'exercise_types'

    def __str__(self):
        return self.name
    

class Exercise(models.Model):
    type = models.ForeignKey(ExerciseType, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True, null=True)
    reccomendation = models.CharField(max_length=500, blank=True, null=True)
    repetition = models.CharField(max_length=500, blank=True, null=True)
    duration = models.CharField(max_length=500, blank=True, null=True)
    rest_period = models.CharField(max_length=500, blank=True, null=True)
    walk = models.CharField(max_length=500, blank=True, null=True)
    achievement = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'exercises'

    def __str__(self):
        return self.name


class WorkoutGoal(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'workout_goals'

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, db_index=True, unique=True)
    name = models.CharField(max_length=100)
    workout_goals = models.ManyToManyField(WorkoutGoal, related_name='workout_plans')
    workout_days = models.ManyToManyField(WorkoutDay, related_name='workout_plans')
    exercises = models.ManyToManyField(Exercise, related_name='workout_plans')
    
    class Meta:
        db_table = 'workout_plans'
   
    def __str__(self):
        return self.name
