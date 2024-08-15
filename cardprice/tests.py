from django.test import TestCase
from cardprice.tasks import refreshTcgSetList
from cardprice.models import TcgPlayerSet
from .tasks import refreshTcgSetList
import environ


# Create your tests here.
class refreshTcgSetListCase(TestCase):
    def setUp(self):
        env = environ.Env()
        environ.Env().read_env()
        refreshTcgSetList()

    def test_load(self):
        ALC1ed = TcgPlayerSet.objects.get(setNameId=23338)
        print(ALC1ed)
        self.assertEqual(ALC1ed.categoryId, 74)
        self.assertEqual(ALC1ed.name, 'Alchemical Revolution')
        self.assertEqual(ALC1ed.urlName, 'alchemical-revolution')
        self.assertEqual(ALC1ed.abbreviation, 'ALC')