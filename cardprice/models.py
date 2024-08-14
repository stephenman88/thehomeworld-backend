from django.db import models

# Create your models here.
class tcgPlayerSet:
    setNameID: models.IntegerField
    categoryID: models.IntegerField
    name: models.CharField(max_length=255)
    cleanSetName: models.CharField(max_length=255)
    urlName: models.CharField(max_length=255)
    abbreviation: models.CharField(max_length=255)
    releaseDate: models.DateTimeField
    active: models.BooleanField

class tcgPlayerCard:
    productID: models.IntegerField
    productConditionID: models.IntegerField
    condition: models.CharField(max_length=255)
    game: models.CharField(max_length=255)
    isSupplemental: models.BooleanField
    lowPrice: models.DecimalField(decimal_places=2)
    marketPrice: models.DecimalField(decimal_places=2)
    