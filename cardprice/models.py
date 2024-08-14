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
    number: models.CharField(max_length=16)
    printing: models.CharField(max_length=32)
    productName: models.CharField(max_length=255)
    rarity: models.CharField(max_length=32)
    sales: models.IntegerField
    
class indexCard:
    uuid: models.UUIDField
    types: models.JSONField
    classes: models.JSONField
    subtypes: models.JSONField
    element: models.CharField(max_length=128)
    name: models.CharField(max_length=128)
    slug: models.CharField(max_length=128)
    effect: models.CharField
    effect_raw: models.CharField
    rule: models.JSONField
    flavor: models.CharField(max_length=255)
    cost_memory: models.IntegerField
    cost_reserve: models.IntegerField
    level: models.IntegerField
    power: models.IntegerField
    life: models.IntegerField
    durability: models.IntegerField
    speed: models.IntegerField
    legality: models.JSONField
    related_ids: models.JSONField
    last_update: models.DateTimeField

class indexEdition:
    uuid: models.UUIDField
    card_id: models.ForeignKey(indexCard, on_delete=models.CASCADE)
    collector_number: models.CharField(max_length=16)
    slug: models.CharField(max_length=255)
    illustrator: models.CharField(max_length=128)
    rarity: models.IntegerField
    effect: models.CharField(max_length=255)
    flavor: models.CharField(max_length=255)
    thema_grace_nonfoil: models.IntegerField
    thema_valor_nonfoil: models.IntegerField
    thema_charm_nonfoil: models.IntegerField
    thema_grace_foil: models.IntegerField
    thema_valor_foil: models.IntegerField
    thema_charm_foil: models.IntegerField
    thema_foil: models.IntegerField
    thema_nonfoil: models.IntegerField
    circulations: models.JSONField
    circulationTemplate: models.ManyToManyField(indexCirculationTemplate)
    set: models.ManyToManyField(indexSet)

class indexCirculationTemplate:
    uuid: models.UUIDField
    name: models.CharField(max_length=32)
    foil: models.BooleanField
    printing: models.BooleanField
    population_operator: models.CharField(max_length=1)
    population: models.IntegerField

class indexSet:
    name: models.CharField(max_length=64)
    prefix: models.CharField(max_length=16)
    language: models.CharField(max_length=16)