import uuid
from django.db import models
from accounts.models import CustomUser

status_choices = (
            ('done', 'done'),
            ('todo', 'to do'),
            ('inprogress', 'in progress'),
        )

class Todos(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    todo_title = models.CharField(max_length=50)
    todo_deadline = models.DateTimeField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.PROJECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=status_choices, max_length=30)

    def __str__(self):
        return self.todo_title

