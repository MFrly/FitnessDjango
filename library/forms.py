from django import forms
from .models import UserProfile, WorkoutPlan, Exercise

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['is_trainer']  # volitelně přidej další např. věk, výška, váha

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['planName', 'finalWeight', 'planDescription']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'gif']
