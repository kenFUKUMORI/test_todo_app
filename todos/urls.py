from django.urls import path
from .views import TodoView

urlpatterns = [
    path('index/', TodoView.as_view()),
]