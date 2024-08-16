from .models import TcgPlayerCard, TcgPlayerSet, IndexCard, IndexEdition, IndexSet
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from .serializers import MergedCardSerializer
import json

# Create your views here.
def buildMergedCardsByName(cardName=""):
    if(type(cardName) != str):
        return {}
    if(type(cardName) == str):
        indexCards = IndexCard.objects.filter(name=cardName)
        if len(indexCards) == 0:
            return {}
        indexCard = indexCards[0]
        mergedCard = {
            'types': indexCard.types,
            'classes': indexCard.classes,
            'subtypes': indexCard.subtypes,
            'element': indexCard.element,
            'name':indexCard.name,
            'slug': indexCard.slug,
            'effect': indexCard.effect_raw,
            'rule': indexCard.rule,
            'flavor': indexCard.flavor,
            'cost_memory': indexCard.cost_memory,
            'cost_reserve': indexCard.cost_reserve,
            'level': indexCard.level,
            'power': indexCard.power,
            'life': indexCard.life,
            'durability': indexCard.durability,
            'speed': indexCard.speed,
            'legality': indexCard.legality,
            'editions': None
        }
        indexEditions = indexCard.indexedition_set.all()
        mergedEditions = []
        for indexEdition in indexEditions:
            abbreviation = indexEdition.set.prefix
            if re.search('^P[0-9][0-9]',abbreviation) != None:
                abbreviation = 'P'
            print(abbreviation)
            print(indexEdition.collector_number)
            tcgCardNonfoil = TcgPlayerCard.objects.filter(setAbbrv=abbreviation, number=indexEdition.collector_number, printing="Normal", condition="Near Mint").exclude(rarity__startswith="Collector")
            tcgCardFoil = TcgPlayerCard.objects.filter(setAbbrv=abbreviation, number=indexEdition.collector_number, printing="Foil", condition="Near Mint Foil").exclude(rarity__startswith="Collector")
            if(re.search("-csr$", indexEdition.slug)):
                tcgCardFoil = TcgPlayerCard.objects.filter(setAbbrv=abbreviation, number=indexEdition.collector_number, rarity="Collector Super Rare")
                tcgCardNonfoil = []
            elif(re.search("-cur$", indexEdition.slug)):
                tcgCardFoil = TcgPlayerCard.objects.filter(setAbbrv=abbreviation, number=indexEdition.collector_number, rarity="Collector Ultra Rare")
                tcgCardNonfoil = []
            mergedEdition = {
                'collector_number': indexEdition.collector_number,
                'slug': indexEdition.slug,
                'illustrator': indexEdition.illustrator,
                'rarity': indexEdition.rarity,
                'effect': indexEdition.effect,
                'flavor': indexEdition.flavor,
                'thema_grace_nonfoil': indexEdition.thema_grace_nonfoil,
                'thema_valor_nonfoil': indexEdition.thema_valor_nonfoil,
                'thema_charm_nonfoil': indexEdition.thema_charm_nonfoil,
                'thema_mystique_nonfoil': indexEdition.thema_mystique_nonfoil,
                'thema_ferocity_nonfoil': indexEdition.thema_ferocity_nonfoil,
                'thema_grace_foil': indexEdition.thema_grace_foil,
                'thema_valor_foil': indexEdition.thema_valor_foil,
                'thema_charm_foil': indexEdition.thema_charm_foil,
                'thema_mystique_foil': indexEdition.thema_mystique_foil,
                'thema_ferocity_foil': indexEdition.thema_ferocity_foil,
                'thema_foil': indexEdition.thema_foil,
                'thema_nonfoil': indexEdition.thema_nonfoil,
                'set_name': indexEdition.set.name,
                'set_prefix': indexEdition.set.prefix,
                'set_language': indexEdition.set.language,
                'tcg_low_nonfoil': None if len(tcgCardNonfoil) < 1 else float(tcgCardNonfoil[0].lowPrice),
                'tcg_market_nonfoil': None if len(tcgCardNonfoil) < 1 else float(tcgCardNonfoil[0].marketPrice),
                'tcg_low_foil': None if len(tcgCardFoil) < 1 else float(tcgCardFoil[0].lowPrice),
                'tcg_market_foil': None if len(tcgCardFoil) < 1 else float(tcgCardFoil[0].marketPrice)
            }
            
            mergedEditions.append(mergedEdition)
        mergedCard['editions'] = mergedEditions
    return mergedCard

def buildMergedCardsStartingWith(cardName=""):
    if(type(cardName) != str):
        return []
    if(type(cardName) == str):
        indexCards = IndexCard.objects.filter(name__startswith=cardName)
        mergedCards = []
        for indexCard in indexCards:
            mergedCard = {
                'types': indexCard.types,
                'classes': indexCard.classes,
                'subtypes': indexCard.subtypes,
                'element': indexCard.element,
                'name':indexCard.name,
                'slug': indexCard.slug,
                'effect': indexCard.effect_raw,
                'rule': indexCard.rule,
                'flavor': indexCard.flavor,
                'cost_memory': indexCard.cost_memory,
                'cost_reserve': indexCard.cost_reserve,
                'level': indexCard.level,
                'power': indexCard.power,
                'life': indexCard.life,
                'durability': indexCard.durability,
                'speed': indexCard.speed,
                'legality': indexCard.legality,
                'editions': []
            }
            indexEditions = indexCard.indexedition_set.all()
            mergedEditions = []
            for indexEdition in indexEditions:
                abbreviation = indexEdition.set.prefix
                if re.search('^P[0-9][0-9]',abbreviation) != None:
                    abbreviation = 'P'
                tcgCardFoil = TcgPlayerCard.objects.filter(setAbbrv=abbreviation, number=indexEdition.collector_number, printing="Foil", condition__startswith="Near Mint")
                tcgCardNonfoil = TcgPlayerCard.objects.filter(setAbbrv=abbreviation, number=indexEdition.collector_number, printing="Normal", condition__startswith="Near Mint")
                mergedEdition = {
                    'collector_number': indexEdition.collector_number,
                    'slug': indexEdition.slug,
                    'illustrator': indexEdition.illustrator,
                    'rarity': indexEdition.rarity,
                    'effect': indexEdition.effect,
                    'flavor': indexEdition.flavor,
                    'thema_grace_nonfoil': indexEdition.thema_grace_nonfoil,
                    'thema_valor_nonfoil': indexEdition.thema_valor_nonfoil,
                    'thema_charm_nonfoil': indexEdition.thema_charm_nonfoil,
                    'thema_mystique_nonfoil': indexEdition.thema_mystique_nonfoil,
                    'thema_ferocity_nonfoil': indexEdition.thema_ferocity_nonfoil,
                    'thema_grace_foil': indexEdition.thema_grace_foil,
                    'thema_valor_foil': indexEdition.thema_valor_foil,
                    'thema_charm_foil': indexEdition.thema_charm_foil,
                    'thema_mystique_foil': indexEdition.thema_mystique_foil,
                    'thema_ferocity_foil': indexEdition.thema_ferocity_foil,
                    'thema_foil': indexEdition.thema_foil,
                    'thema_nonfoil': indexEdition.thema_nonfoil,
                    'set_name': indexEdition.set.name,
                    'set_prefix': indexEdition.set.prefix,
                    'set_language': indexEdition.set.language,
                    'tcg_low_nonfoil': None if len(tcgCardNonfoil) < 1 else tcgCardNonfoil[0].lowPrice,
                    'tcg_market_nonfoil': None if len(tcgCardNonfoil) < 1 else tcgCardNonfoil[0].marketPrice,
                    'tcg_low_foil': None if len(tcgCardFoil) < 1 else tcgCardFoil[0].lowPrice,
                    'tcg_market_foil': None if len(tcgCardFoil) < 1 else tcgCardFoil[0].marketPrice
                }
                mergedEditions.append(mergedEdition)
            mergedCard['editions'] =mergedEditions
            mergedCards.append(mergedCard)
        return mergedCards

class SingleCardSearch(APIView):
    def get(self, request, *args, **kwargs):
        nameValue = request.query_params.get('name')
        print(nameValue)
        result = buildMergedCardsByName(nameValue)
        serializer = MergedCardSerializer(data=result)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)