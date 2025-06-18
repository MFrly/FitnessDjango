from django import forms
from .models import UserProfile, WorkoutPlan, Exercise, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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


class CustomSignupForm(UserCreationForm):
    age = forms.IntegerField(required=True, label='Věk')
    height = forms.FloatField(required=True, label='Výška (cm)')
    weight = forms.FloatField(required=True, label='Váha (kg)')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age', 'height', 'weight']