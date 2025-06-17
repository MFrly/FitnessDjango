from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('accounts/signup/', views.SignupView.as_view(), name='signup'),
    path('registration/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('registration/', include('django.contrib.auth.urls')),

    path('profiles/', views.UserProfileListView.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', views.UserProfileDetailView.as_view(), name='userprofile-detail'),

    path('trainers/', views.TrainerListView.as_view(), name='trainer-list'),
    path('exercises/', views.ExerciseListView.as_view(), name='exercise-list'),
    path('workout-plans/', views.WorkoutPlanListView.as_view(), name='workoutplan-list'),
    path('workout-plans/<int:pk>/', views.WorkoutPlanDetailView.as_view(), name='workoutplan-detail'),

    path('workout-plans/create/', views.WorkoutPlanCreateView.as_view(), name='workoutplan-create'),
    path('exercises/create/', views.ExerciseCreateView.as_view(), name='exercise-create'),
    path('workout-plans/<int:pk>/delete/', views.WorkoutPlanDeleteView.as_view(), name='workoutplan-delete'),
    path('exercises/<int:pk>/delete/', views.ExerciseDeleteView.as_view(), name='exercise-delete'),
]
