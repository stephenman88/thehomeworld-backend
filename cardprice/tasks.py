from celery import shared_task
from .models import TcgPlayerSet
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
