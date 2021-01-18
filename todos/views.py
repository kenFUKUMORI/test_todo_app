from django.shortcuts import render
from django.views import View

class TodoView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'test': 'test_message',
        }
        return render(request, 'todos/index.html', context)


todo_views = TodoView.as_view()