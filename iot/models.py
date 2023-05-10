from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    flag = models.BooleanField(default= True)

    def __str__(self):
        return self.name