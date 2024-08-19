from celery import shared_task
from .models import TcgPlayerSet, TcgPlayerCard, IndexCard, IndexEdition, IndexSet
import requests
import environ

env = environ.Env()
environ.Env().read_env()

TCGPLAYER_SETNAMES_URL = env('TCGPLAYER_SETNAMES_URL')
CARDPRICEURL = env('TCGPLAYER_CARDPRICE_URL_SAMPLE')

@shared_task
def refreshTcgSetList():
    response = requests.get(env('TCGPLAYER_SETNAMES_URL'))
    for set in response.json()['results']:
        dataObject, isCreated =TcgPlayerSet.objects.update_or_create(
                setNameId=set['setNameId'],
                defaults=set
            )
        dataObject.save()
    print('TCG Player set list updated')

@shared_task
def refreshTcgCardPrice():
    setList = TcgPlayerSet.objects.all()
    if len(list(setList)) == 0:
        refreshTcgSetList()
        setList = TcgPlayerSet.objects.all()
    for set in setList:
        url = env('TCGPLAYER_CARDPRICE_BASE_URL') + str(set.setNameId) + env('TCGPLAYER_CARDPRICE_QUERY')
        response = requests.get(url)
        if 'result' in response.json():
            result = response.json()['result']
            for card in result:
                dataObject, isCreated = TcgPlayerCard.objects.update_or_create(
                    productID=card['productID'],
                    condition=card['condition'],
                    number=card['number'],
                    printing=card['printing'],
                    setAbbrv=card['setAbbrv'],
                    defaults=card
                )
                dataObject.save()
    print('TCG Player card list updated')

@shared_task
def refreshIndexCard(page=1):
    url = env('INDEX_CARD_BASE_URL') + str(page)
    response = requests.get(url)
    if ('data' in response.json()):
        data = response.json()['data']
        for card in data:
            cardObject, isCreated = IndexCard.objects.update_or_create(
                uuid=card['uuid'],
                defaults={
                    'uuid':card['uuid'],
                    'types':card['types'],
                    'classes':card['classes'],
                    'subtypes':card['subtypes'],
                    'element':card['element'],
                    'name':card['name'],
                    'slug':card['slug'],
                    'effect':card['effect'],
                    'effect_raw':card['effect_raw'],
                    'rule':card['rule'],
                    'flavor':card['flavor'],
                    'cost_memory':card['cost_memory'],
                    'cost_reserve':card['cost_reserve'],
                    'level':card['level'],
                    'power':card['power'],
                    'life':card['life'],
                    'durability':card['durability'],
                    'speed':card['speed'],
                    'legality':card['legality'],
                    'related_ids':card['related_ids'],
                    'last_update':card['last_update']
                }
            )
            cardObject.save()
            editions = card['result_editions']
            for edition in editions:
                if 'set' in edition:
                    setData = edition['set']
                    gaSet, gaSetCreated = IndexSet.objects.update_or_create(
                        name=setData['name'],
                        defaults=setData
                    )
                    gaSet.save()

                    defaults={
                        'collector_number':edition['collector_number'],
                        'slug':edition['slug'],
                        'illustrator':edition['illustrator'],
                        'rarity':edition['rarity'],
                        'effect':edition['effect'],
                        'flavor':edition['flavor'],
                        'thema_grace_nonfoil':edition['thema_grace_nonfoil'],
                        "thema_valor_nonfoil": edition['thema_valor_nonfoil'],
                        "thema_charm_nonfoil": edition['thema_charm_nonfoil'],
                        "thema_mystique_nonfoil": edition['thema_mystique_nonfoil'],
                        "thema_ferocity_nonfoil": edition['thema_ferocity_nonfoil'],
                        "thema_grace_foil": edition['thema_grace_foil'],
                        "thema_valor_foil": edition['thema_valor_foil'],
                        "thema_charm_foil": edition['thema_charm_foil'],
                        "thema_mystique_foil": edition['thema_mystique_foil'],
                        "thema_ferocity_foil": edition['thema_ferocity_foil'],
                        "thema_foil": edition['thema_foil'],
                        "thema_nonfoil": edition['thema_nonfoil'],
                        "circulations": edition['circulations'],
                        'circulationTemplates': edition['circulationTemplates']
                        }
                    try:
                        editionObj = IndexEdition.objects.get(uuid=edition['uuid'])
                        for key, value in defaults.items():
                            setattr(editionObj, key, value)
                        setattr(editionObj, 'card', cardObject)
                        setattr(editionObj, 'set', gaSet)
                        editionObj.save()
                    except IndexEdition.DoesNotExist:
                        editionObj = IndexEdition.objects.create(
                            card=cardObject,
                            uuid=edition['uuid'],
                            collector_number=edition['collector_number'],
                            slug=edition['slug'],
                            illustrator=edition['illustrator'],
                            rarity=edition['rarity'],
                            effect=edition['effect'],
                            flavor=edition['flavor'],
                            thema_grace_nonfoil=edition['thema_grace_nonfoil'],
                            thema_valor_nonfoil= edition['thema_valor_nonfoil'],
                            thema_charm_nonfoil= edition['thema_charm_nonfoil'],
                            thema_mystique_nonfoil= edition['thema_mystique_nonfoil'],
                            thema_ferocity_nonfoil= edition['thema_ferocity_nonfoil'],
                            thema_grace_foil= edition['thema_grace_foil'],
                            thema_valor_foil= edition['thema_valor_foil'],
                            thema_charm_foil= edition['thema_charm_foil'],
                            thema_mystique_foil= edition['thema_mystique_foil'],
                            thema_ferocity_foil= edition['thema_ferocity_foil'],
                            thema_foil= edition['thema_foil'],
                            thema_nonfoil= edition['thema_nonfoil'],
                            circulations= edition['circulations'],
                            circulationTemplates= edition['circulationTemplates'],
                            set=gaSet
                        )
                        editionObj.save()
        if('has_more' in response.json() and response.json()['has_more'] == True):
            refreshIndexCard(page+1)
    print('GA Index Card list updated')