from django.db import models


STRENGTH_LEVEL = [
     ('5', 'Up to 5% alcohol'),
     ('7', 'Up to 7% alcohol'),
     ('12', 'Up to 12% alcohol'),
     ('40', 'Up to 40% alcohol'),
]


SKILL_LEVEL = [
     ('0', 'Beginner'),
     ('1', 'Skilled'),
     ('2', 'Specialist'),
     ('3', 'Expert'),
]


class Cocktail(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=500
    )
    publication_date = models.DateTimeField(),
    description = models.CharField(
        verbose_name="Description",
        max_length=1000
    )
    is_alcoholic = models.BooleanField(
        verbose_name="Is alcoholic",
        default=True
    ),
    skill_level = models.CharField(
        verbose_name="Skill Level",
        max_length=1,
        choices=SKILL_LEVEL,
        default=''
    )
    strength_level = models.CharField(
        verbose_name="Strength",
        max_length=2,
        choices=STRENGTH_LEVEL,
        default=''
    )
    cocktail_category = models.ForeignKey('CocktailCategory', on_delete=models.SET_NULL, null=True)
    flavor = models.ForeignKey('Flavor', related_name='cocktails', on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(
        "cocktails_app.Ingredient",
    )

    def __str__(self):
        return self.name
