from celery import shared_task
from .models import TcgPlayerSet, TcgPlayerCard
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

@shared_task
def refreshTcgCardPrice():
    setList = TcgPlayerSet.objects.all()
    if len(setList) == 0:
        refreshTcgSetList()
    for set in setList:
        url = env('TCGPLAYER_CARDPRICE_BASE_URL') + str(set.setNameId) + env('TCGPLAYER_CARDPRICE_QUERY')
        response = requests.get(url)
        if 'result' in response.json():
            result = response.json()['result']
            for card in result:
                dataObject, isCreated = TcgPlayerCard.objects.update_or_create(
                    productID=card['productID'],
                    defaults=card
                )
                dataObject.save()