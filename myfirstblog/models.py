from django.db import models

class Post(models.Model):
    tittle = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.tittle
