from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from accounts.models import CustomUser

from .models import Todo
from .forms import TodoForm

class MyTodoView(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user
        todo_list = Todo.objects.filter(user_id=user_id)
        context = {
            'test': 'test_message',
        }
        print(todo_list)
        return render(request, 'todos/index.html', {'return_todo_list': todo_list})

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name= "todos/form.html"
    success_url = "/todo/list"

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super(TodoCreateView, self).form_valid(form)

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = "/todo/list"


todo_views = MyTodoView.as_view()