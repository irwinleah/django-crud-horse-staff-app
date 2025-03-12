from django.db import models
from django.urls import reverse

class Horse(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse('horse-detail', kwargs={'horse_id': self.id})
    
    def __str__(self):
        return self.name

TIMES = (
    ("A", "AM"),
    ("P", "PM"),
)

GRAINS = (
    ("WL", "Weanling"),
    ("YL", "Yearling"),
    ("WK", "Working"),
    ("MT", "Maintenance"),
    ("SR", "Senior"),
)

class Feeding(models.Model):
    date = models.DateField()
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    grain_type = models.CharField(
        max_length=2,
        choices=GRAINS,
        default=GRAINS[0][0]
    )

    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Training(models.Model):
    locaton = models.CharField(max_length=100)
    discipline = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.discipline} at {self.locaton}"
    
    def get_absolute_url(self):
        return reverse('training-detail', kwargs={'pk': self.id})