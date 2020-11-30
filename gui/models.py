from django.db import models


# Create your models here.
class ProgramGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(str(self.id), self.name)


class Program(models.Model):
    name = models.CharField(max_length=255)
    pid = models.IntegerField()
    group = models.ForeignKey(ProgramGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(str(self.id), self.name)
