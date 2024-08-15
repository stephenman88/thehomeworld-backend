from django.test import TestCase
from cardprice.tasks import refreshTcgSetList
from cardprice.models import TcgPlayerSet, TcgPlayerCard
from .tasks import refreshTcgSetList, refreshTcgCardPrice
import environ


# Create your tests here.
class refreshTcgSetListCase(TestCase):
    def setUp(self):
        refreshTcgSetList()

    def test_load(self):
        ALC1ed = TcgPlayerSet.objects.get(setNameId=23338)
        print(ALC1ed)
        self.assertEqual(ALC1ed.categoryId, 74)
        self.assertEqual(ALC1ed.name, 'Alchemical Revolution')
        self.assertEqual(ALC1ed.urlName, 'alchemical-revolution')
        self.assertEqual(ALC1ed.abbreviation, 'ALC')

class refreshTcgCardPriceCase(TestCase):
    def setUp(self):
        refreshTcgSetList()
        refreshTcgCardPrice()

    def test_aeson_protector(self):
        aesan = TcgPlayerCard.objects.get(productID=494615)
        print(aesan.productName)
        self.assertEqual(aesan.game, "Grand Archive")
        self.assertEqual(aesan.productName, 'Aesan Protector')
        self.assertEqual(aesan.rarity, 'Uncommon')
        print(aesan.lowPrice)
        print(type(aesan.lowPrice))
        print(aesan.marketPrice)
        print(type(aesan.marketPrice))

    def test_nico(self):
        nico = TcgPlayerCard.objects.get(productID=531610, condition="Near Mint")
        print(nico.productName)
        self.assertEqual(nico.set, "Alchemical Revolution")
        self.assertEqual(nico.productName, 'Nico, Whiplash Allure')
        self.assertEqual(nico.rarity, 'Uncommon')
        print(nico.lowPrice)
        print(type(nico.lowPrice))
        print(nico.marketPrice)
        print(type(nico.marketPrice))
