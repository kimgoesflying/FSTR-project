from django.urls import path
from .views import ListTourists, DetailTourist

urlpatterns = [
    path('', ListTourists.as_view()),
    path('<int:pk>/', DetailTourist.as_view()),
]
