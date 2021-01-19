from django.urls import path
from .views import MyTodoView, TodoCreateView, TodoDeleteView

urlpatterns = [
    path('list/', MyTodoView.as_view()),
    path('create/', TodoCreateView.as_view()),
    path('<int:pk>/delete', TodoDeleteView.as_view(),name='delete'),
    ]