from django.urls import path
from .views import MyTodoView

urlpatterns = [
    path('list/', MyTodoView.as_view()),
]