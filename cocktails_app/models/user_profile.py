from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    favourites = models.ManyToManyField(
        "cocktails_app.Cocktail",
    )

    def __str__(self):
        return self.user.username

