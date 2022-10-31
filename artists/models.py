from django.db import models

# Create your models here.


class Artist(models.Model):
    stage_name = models.CharField(blank=False, unique=True, max_length=255)
    social_link_field = models.URLField(max_length=255, blank=True)