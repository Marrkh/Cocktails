from rest_framework import serializers
from .models import Cocktail, CocktailCategory, Flavor, Ingredient, IngredientCategory, UserProfile


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


class CocktailCategorySerializer(serializers.ModelSerializer):
    # cocktails = serializers.SerializerMethodField('get_cocktails')

    # def get_cocktails(self, cocktail):
    #     queryset = Cocktail.objects.filter(cocktail_category=self.instance)
    #     serializer = CocktailSerializer(instance=queryset, many=True)
    #     return serializer.data

    class Meta:
        model = CocktailCategory
        fields = '__all__'


class CocktailSerializer(serializers.ModelSerializer):
    cocktail_category = CocktailCategorySerializer(read_only=True)

    class Meta:
        model = Cocktail
        fields = '__all__'

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = '__all__'

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class IngredientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientCategory
        fields = '__all__'

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass











