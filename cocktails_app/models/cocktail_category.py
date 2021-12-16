from django.db import models


class CocktailCategory(models.Model):
    class Meta:
        verbose_name = "Cocktail category"
        verbose_name_plural = "Cocktail categories"
    name = models.CharField(
        verbose_name="Name",
        max_length=500
    )

    def __str__(self):
        return self.name

