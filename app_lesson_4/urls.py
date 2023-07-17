from django.urls import path
from . import views

urlpatterns = [
    path("", views.app_lesson_4, name="app_lesson_4")
]