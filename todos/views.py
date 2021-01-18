from django.shortcuts import render
from django.views import View
from .models import Todo


class MyTodoView(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user
        todo_list = Todo.objects.filter(user_id=user_id)
        context = {
            'test': 'test_message',
        }
        print(todo_list)
        return render(request, 'todos/index.html', {'return_todo_list': todo_list})


todo_views = MyTodoView.as_view()