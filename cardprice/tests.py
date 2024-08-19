from django.test import TestCase
from cardprice.tasks import refreshTcgSetList
from cardprice.models import TcgPlayerSet, TcgPlayerCard, IndexCard, IndexEdition, IndexSet
from .views import buildMergedCardsByName, buildMergedCardsStartingWith
from .tasks import refreshTcgSetList, refreshTcgCardPrice, refreshIndexCard
import environ


# Create your tests here.
'''class refreshTcgSetListCase(TestCase):
    def setUp(self):
        refreshTcgSetList()

    def test_load(self):
        ALC1ed = TcgPlayerSet.objects.get(setNameId=23338)
        print(ALC1ed)
        self.assertEqual(ALC1ed.categoryId, 74)
        self.assertEqual(ALC1ed.name, 'Alchemical Revolution')
        self.assertEqual(ALC1ed.urlName, 'alchemical-revolution')
        self.assertEqual(ALC1ed.abbreviation, 'ALC')'''

'''class refreshTcgCardPriceCase(TestCase):
    def setUp(self):
        refreshTcgSetList()
        refreshTcgCardPrice()

    def test_aeson_protector(self):
        aesan = TcgPlayerCard.objects.get(setAbbrv="ALCSD", number="070", printing="Normal", condition__startswith="Near Mint")
        print(aesan.productName)
        self.assertEqual(aesan.game, "Grand Archive")
        self.assertEqual(aesan.productName, 'Airship Engineer')
        self.assertEqual(aesan.rarity, 'Common')
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
        print(type(nico.marketPrice))'''

'''class refreshIndexCardCase(TestCase):
    def setUp(self):
        refreshIndexCard()

    def test_spirit_of_water_card(self):
        spirit_of_water= IndexCard.objects.filter(name="Spirit of Water")
        print(spirit_of_water[0].name)
        self.assertEqual(len(spirit_of_water), 1)
        self.assertListEqual(spirit_of_water[0].types, ["CHAMPION"])
        self.assertListEqual(spirit_of_water[0].classes, ["SPIRIT"])
        self.assertListEqual(spirit_of_water[0].subtypes, ["SPIRIT"])
        self.assertEqual(spirit_of_water[0].effect_raw, "On Enter: Draw seven cards.")
        print(type(spirit_of_water[0].rule))
        self.assertEqual(spirit_of_water[0].rule, None)
        self.assertEqual(spirit_of_water[0].flavor, "Convalescing waves cascade through the soul, revitalizing the body and mind from the depths. ")
        self.assertEqual(spirit_of_water[0].cost_memory, 0)
        self.assertEqual(spirit_of_water[0].level, 0)
        self.assertEqual(spirit_of_water[0].life, 15)

        spirit_of_water_ed = spirit_of_water[0].indexedition_set.all()
        self.assertEqual(len(spirit_of_water_ed), 6)
        self.assertEqual(spirit_of_water_ed[5].uuid, 'qocl33ms0k')
        self.assertEqual(spirit_of_water_ed[0].set.name, 'Alchemical Revolution')
        print(spirit_of_water_ed[0].set.name)
        self.assertEqual(spirit_of_water_ed[1].set.name, 'Alchemical Revolution Starter Decks')
        self.assertEqual(spirit_of_water_ed[2].set.name, 'Dawn of Ashes Alter Edition')
        self.assertEqual(spirit_of_water_ed[3].set.name, 'Dawn of Ashes First Edition')
        self.assertEqual(spirit_of_water_ed[4].set.name, 'Dawn of Ashes Starter Decks')'''

class buildMergedCard(TestCase):
    def setUp(self):
        refreshTcgCardPrice()
        refreshIndexCard()

    def test_build_merged_card(self):
        mergedCard = buildMergedCardsByName(cardName="Airship Engineer")[0]
        self.assertEqual(mergedCard['name'], "Airship Engineer")
        self.assertEqual(mergedCard['cost_memory'], None)
        self.assertEqual(mergedCard['cost_reserve'], 2)
        self.assertEqual(mergedCard['editions'][1]['slug'], 'airship-engineer-alcsd')
        print(mergedCard['editions'][1]['tcg_low_nonfoil'])
        #self.assertEqual(mergedCard['editions'][1]['tcg_low_nonfoil'], 0.15)
        self.assertEqual(mergedCard['editions'][1]['tcg_low_foil'], None)

        mergedCard = buildMergedCardsByName(cardName="Nimue, Cursed Touch")[0]
        self.assertEqual(mergedCard['name'], "Nimue, Cursed Touch")
        self.assertEqual(mergedCard['cost_memory'], None)
        self.assertEqual(mergedCard['cost_reserve'], 2)
        self.assertEqual(mergedCard['editions'][2]['slug'], 'nimue-cursed-touch-doap-ks')
        print(mergedCard['editions'][2]['tcg_low_nonfoil'])
        self.assertEqual(mergedCard['editions'][2]['tcg_low_nonfoil'], 3.45)
        self.assertEqual(mergedCard['editions'][2]['tcg_low_foil'], 3.67)