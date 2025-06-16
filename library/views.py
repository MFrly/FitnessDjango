from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import UserProfile, WorkoutPlan, Exercise, WorkoutExercise
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

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
    template_name = 'trainer-list.html'

    def get_queryset(self):
        # Return only users who are trainers
        return UserProfile.objects.filter(is_trainer=True)
    
class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'accounts/signup.html', {'form': form})