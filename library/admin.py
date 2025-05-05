from django.contrib import admin
from .models import UserProfile, WorkoutPlan ,WorkoutExercise, Exercise

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutExercise)
admin.site.register(Exercise)