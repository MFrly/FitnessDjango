from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
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

@login_required
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'profile': profile})

class TrainerListView(ListView):
    model = UserProfile
    template_name = 'trainer_list.html'

    def get_queryset(self):
        # Return only users who are trainers
        return UserProfile.objects.filter(is_trainer=True)
