from django.urls import path
from .views import ListMountainPass, DetailMountainPass

urlpatterns = [
    path('', ListMountainPass.as_view()),
    path('<int:pk>/', DetailMountainPass.as_view()),
]
