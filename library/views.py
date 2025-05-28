from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import UserProfile, WorkoutPlan, Exercise, WorkoutExercise

def index(request):
    return render(request, 'index.html')
class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'userprofile_list.html'


class WorkoutPlanListView(ListView):
    model = WorkoutPlan
    template_name = 'workoutplan_list.html'


class WorkoutPlanDetailView(DetailView):
    model = WorkoutPlan
    template_name = 'workoutplan_detail.html'


class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
