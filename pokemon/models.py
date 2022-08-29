from django.db import models
from django.contrib.auth import get_user_model

class Pokemon(models.Model):
    species = models.CharField(max_length=24)
    name = models.CharField(max_length=24)
    level = models.IntegerField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    caught = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name