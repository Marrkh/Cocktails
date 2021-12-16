from django.db import models


class Flavor(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=500
    )

    def __str__(self):
        return self.name

