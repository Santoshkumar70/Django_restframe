from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=100)
    esal = models.FloatField()

    

    def __str__(self):
        return f"{self.eid}--{self.ename}"
