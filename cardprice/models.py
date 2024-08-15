from django.db import models

# Create your models here.
class TcgPlayerSet(models.Model):
    setNameId= models.IntegerField()
    categoryId= models.IntegerField()
    name= models.CharField(max_length=255)
    cleanSetName= models.CharField(max_length=255)
    urlName= models.CharField(max_length=255)
    abbreviation= models.CharField(max_length=255)
    releaseDate= models.DateTimeField(null=True)
    active= models.BooleanField()

class TcgPlayerCard(models.Model):
    productId= models.IntegerField()
    productConditionId= models.IntegerField()
    condition= models.CharField(max_length=255)
    game= models.CharField(max_length=255)
    isSupplemental= models.BooleanField()
    lowPrice= models.DecimalField(decimal_places=2, max_digits=100)
    marketPrice= models.DecimalField(decimal_places=2, max_digits=100)
    number= models.CharField(max_length=16)
    printing= models.CharField(max_length=32)
    productName= models.CharField(max_length=255)
    rarity= models.CharField(max_length=32)
    sales= models.IntegerField
    
class IndexCard(models.Model):
    uuid= models.UUIDField()
    types= models.JSONField()
    classes= models.JSONField()
    subtypes= models.JSONField()
    element= models.CharField(max_length=128)
    name= models.CharField(max_length=128)
    slug= models.CharField(max_length=128)
    effect= models.CharField(null=True)
    effect_raw= models.CharField(null=True)
    rule= models.JSONField(null=True)
    flavor= models.CharField(max_length=255, null=True)
    cost_memory= models.IntegerField(null=True)
    cost_reserve= models.IntegerField(null=True)
    level= models.IntegerField(null=True)
    power= models.IntegerField(null=True)
    life= models.IntegerField(null=True)
    durability= models.IntegerField(null=True)
    speed= models.BooleanField(null=True)
    legality= models.JSONField(null=True)
    related_ids= models.JSONField(null=True)
    last_update= models.DateTimeField()

    
class IndexCirculationTemplate(models.Model):
    uuid= models.UUIDField()
    name= models.CharField(max_length=32)
    foil= models.BooleanField()
    printing= models.BooleanField()
    population_operator= models.CharField(max_length=1)
    population= models.IntegerField

class IndexSet(models.Model):
    name= models.CharField(max_length=64)
    prefix= models.CharField(max_length=16)
    language= models.CharField(max_length=16)

class IndexEdition(models.Model):
    uuid= models.UUIDField()
    card_id= models.ForeignKey(IndexCard, on_delete=models.CASCADE)
    collector_number= models.CharField(max_length=16)
    slug= models.CharField(max_length=255)
    illustrator= models.CharField(max_length=128)
    rarity= models.IntegerField()
    effect= models.CharField(max_length=255, null=True)
    flavor= models.CharField(max_length=255, null=True)
    thema_grace_nonfoil= models.IntegerField()
    thema_valor_nonfoil= models.IntegerField()
    thema_charm_nonfoil= models.IntegerField()
    thema_grace_foil= models.IntegerField()
    thema_valor_foil= models.IntegerField()
    thema_charm_foil= models.IntegerField()
    thema_foil= models.IntegerField()
    thema_nonfoil= models.IntegerField()
    circulations= models.JSONField()
    circulationTemplate= models.ManyToManyField(IndexCirculationTemplate)
    set= models.ManyToManyField(IndexSet)