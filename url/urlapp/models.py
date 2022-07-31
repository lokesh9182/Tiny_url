from django.db import models

# Create your models here.
class urltable(models.Model):
    slno=models.IntegerField(null=True)
    shorturl=models.CharField(max_length=100)
    longurl= models.CharField(max_length=300)

    def __str__(self):
        return self.shorturl