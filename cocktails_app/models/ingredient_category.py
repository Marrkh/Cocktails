from django.db import models


class IngredientCategory(models.Model):
    class Meta:
        verbose_name = "Ingredient category"
        verbose_name_plural = "Ingredient categories"
    name = models.CharField(
        verbose_name="Name",
        max_length=500
    )

    def __str__(self):
        return self.name

