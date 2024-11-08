from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30)
    opening_date = models.DateField()
    running_time = models.IntegerField()
    overview = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=30)
    star = models.IntegerField()
    comment = models.CharField(null=True, max_length=100)
    created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.comment
