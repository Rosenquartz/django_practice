from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def fakedelete(self):
        self.title = 'Deleted! Haha!'
        print('hehe')
        return