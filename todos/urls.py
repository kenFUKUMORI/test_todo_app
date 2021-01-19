from django.urls import path
from .views import MyTodoView, TodoCreateView

urlpatterns = [
    path('list/', MyTodoView.as_view()),
    path('create/', TodoCreateView.as_view())
,]