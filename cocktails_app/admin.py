from django.contrib import admin
from cocktails_app.models.cocktail import Cocktail
from cocktails_app.models.cocktail_category import CocktailCategory
from cocktails_app.models.flavor import Flavor
from cocktails_app.models.ingredient import Ingredient
from cocktails_app.models.ingredient_category import IngredientCategory
from cocktails_app.models.user_profile import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "list_favorite_cocktails"]
    readonly_fields = ['list_favorite_cocktails']

    def list_favorite_cocktails(self, instance):
        cocktails = instance.favourites.all()
        cocktail_list = []
        for cocktail in cocktails:
            cocktail_list.append(cocktail.name)
        return ", ".join(cocktail_list)


class CocktailAdmin(admin.ModelAdmin):
    pass


class CocktailCategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    list_filter = ['name']


class FlavorAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    list_filter = ['name']


class IngredientAdmin(admin.ModelAdmin):
    pass


class IngredientCategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    list_filter = ['name']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CocktailCategory, CocktailCategoryAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientCategory, IngredientCategoryAdmin)
