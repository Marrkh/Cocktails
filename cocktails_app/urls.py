from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


urlpatterns = [
    path('cocktails/', views.cocktail_list),
    path('cocktail-categories/', views.cocktail_category_list),
    path('flavors/', views.flavor_list),
    path('ingredients/', views.ingredient_list),
    path('ingredient-categories/', views.ingredient_category_list),
]

# cocktail search by name
# cocktail all data by id or name
# ingredient by name
# ingredient
#
#
# filter cocktail by alcohol level
# filter cocktail by skill level
# filter cocktail by category
