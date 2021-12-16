from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Cocktail, CocktailCategory, Flavor, Ingredient, IngredientCategory
from .serializers import CocktailSerializer, CocktailCategorySerializer, FlavorSerializer, IngredientSerializer, IngredientCategorySerializer


@api_view(['GET'])
def flavor_list(request):
    queryset = Flavor.objects.all().order_by('name')
    serializer = FlavorSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cocktail_list(request):
    print(Cocktail.objects.all())
    queryset = Cocktail.objects.all().order_by('name')
    serializer = CocktailSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cocktail_category_list(request):
    queryset = Cocktail.objects.all().order_by('name')
    serializer = CocktailCategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ingredient_list(request):
    queryset = Ingredient.objects.all().order_by('name')
    serializer = IngredientSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ingredient_category_list(request):
    queryset = IngredientCategory.objects.all().order_by('name')
    serializer = IngredientCategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def flavor_create(request):
    serializer = FlavorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



