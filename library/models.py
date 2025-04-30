import datetime

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(max_length=2, verbose_name='Age')
    height = models.FloatField(max_length=3, verbose_name='Height (cm)', error_messages={'max_length': 'Height must be in cm'})
    weight = models.FloatField(max_length=3, verbose_name='Weight (kg)', error_messages={'max_length': 'Weight must be in kg'})
    
    class Meta:
        ordering = ['name']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        
    def __str__(self):
        return self.name
    
class WorkoutPlan(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workout_plans')
    planName = models.CharField(max_length=100, verbose_name='Plan Name')
    finalWeight = models.FloatField(max_length=3, verbose_name='Final Weight (kg)', error_messages={'max_length': 'Weight must be in kg'})
    planDescription = models.TextField(blank=True, verbose_name='Plan Description')
    
    class Meta:
        ordering = ['planName']
        verbose_name = 'Workout Plan'
        verbose_name_plural = 'Workout Plans'
        
    def __str__(self):
        return self.planName
    
class AllExercises(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    sets = models.IntegerField(help_text='Number of sets')
    reps = models.IntegerField(help_text='Number of reps')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'
        
    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Exercise Name')
    description = models.TextField(blank=True, verbose_name='Exercise Description')
    gif = models.ImageField(upload_to='exercise_gifs/', blank=True, verbose_name='Exercise GIF')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'
        
    def __str__(self):
        return self.name