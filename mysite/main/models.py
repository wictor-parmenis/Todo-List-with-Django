from django.db import models


# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    status = models.BooleanField()

    def __str__(self):
        return self.text

