from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=500
    )
    ingredient_category = models.ForeignKey('IngredientCategory', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

