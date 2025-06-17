from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from .models import UserProfile, WorkoutPlan, Exercise, WorkoutExercise
from .forms import UserProfileForm, WorkoutPlanForm, ExerciseForm

def index(request):
    return render(request, 'index.html')

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'userprofile_list.html'

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userprofile_detail.html'

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
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profile.html', {'profile': profile, 'form': form})

class TrainerListView(ListView):
    model = UserProfile
    template_name = 'trainer-list.html'

    def get_queryset(self):
        return UserProfile.objects.filter(is_trainer=True)

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
        return render(request, 'accounts/signup.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class WorkoutPlanCreateView(CreateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    template_name = 'workoutplan_form.html'
    success_url = reverse_lazy('workoutplan-list')

    def form_valid(self, form):
        form.instance.user_profile = self.request.user.profile
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ExerciseCreateView(CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercise_form.html'
    success_url = reverse_lazy('exercise-list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.profile.is_trainer:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class WorkoutPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkoutPlan
    template_name = 'workoutplan_confirm_delete.html'
    success_url = reverse_lazy('workoutplan-list')


class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = Exercise
    template_name = 'exercise_confirm_delete.html'
    success_url = reverse_lazy('exercise-list')