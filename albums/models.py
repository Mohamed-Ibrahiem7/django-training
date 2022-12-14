from django.db import models
from artists.models import Artist
from django.utils import timezone

# Create your models here.


class Album(models.Model):
    artist = models.ForeignKey(Artist, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="New Album")
    creation_datetime = models.DateTimeField(default=timezone.now)
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(
        default=True, help_text='Approve the album if its name is not explicit')

    def __str__(self):
        return (f"name = {self.name} || creation_datetime = {self.creation_datetime} || release_datetime = {self.release_datetime} || cost = {self.cost}")