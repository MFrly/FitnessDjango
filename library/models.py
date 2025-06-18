from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(verbose_name='Age')
    height = models.FloatField(verbose_name='Height (cm)')
    weight = models.FloatField(verbose_name='Weight (kg)')
    is_trainer = models.BooleanField(default=False, verbose_name='Is Trainer')
    trainer = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'is_trainer': True},
        related_name='clients',
        verbose_name='Selected Trainer'
    )


    class Meta:
        ordering = ['user__username']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username


class WorkoutPlan(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workout_plans')
    planName = models.CharField(max_length=100, verbose_name='Plan Name')
    finalWeight = models.FloatField(verbose_name='Final Weight (kg)')
    planDescription = models.TextField(blank=True, verbose_name='Plan Description')


    class Meta:
        ordering = ['planName']
        verbose_name = 'Workout Plan'
        verbose_name_plural = 'Workout Plans'

    def __str__(self):
        return self.planName


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


class WorkoutExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='workout_usages')
    sets = models.IntegerField(help_text='Number of sets')
    reps = models.IntegerField(help_text='Number of reps')

    class Meta:
        ordering = ['exercise__name']
        verbose_name = 'Workout Exercise'
        verbose_name_plural = 'Workout Exercises'

    def __str__(self):
        return f"{self.exercise.name} - {self.sets}x{self.reps}"
