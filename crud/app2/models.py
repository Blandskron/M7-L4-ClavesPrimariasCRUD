from django.db import models
from app1.models import ParentModel

class ChildModel(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description
