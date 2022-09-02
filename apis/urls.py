from django.urls import path
from .views import ListMountainPass, DetailMountainPass

urlpatterns = [
    path('', ListMountainPass.as_view(), name='list_mountain_pass'),
    path('<int:pk>/', DetailMountainPass.as_view()),
]
