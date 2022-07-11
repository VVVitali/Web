from django.db import models

class Task(models.Model):
    title = models.CharField("Название", max_length= 50)
    task = models.TextField("Описание")
    author = models.CharField("Автор", max_length= 30)


    def __str__(self):
        return self.title
