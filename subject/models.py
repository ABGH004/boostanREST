from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name
