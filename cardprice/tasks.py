from celery import shared_task

SETNAMESURL = 'https://mpapi.tcgplayer.com/v2/Catalog/SetNames?categoryId=74&mpfev=2638'

CARDPRICEURL = 'https://infinite-api.tcgplayer.com/priceguide/set/23128/cards/?rows=5000&productTypeID=122'

@shared_task
def refreshSetList():
    pass

