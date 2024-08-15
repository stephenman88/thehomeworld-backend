from rest_framework import serializers
from .models import TcgPlayerSet, TcgPlayerCard, IndexSet, IndexCard, IndexEdition, IndexCirculationTemplate

class TcgPlayerSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcgPlayerSet
        fields = (
            'setNameId',
            'categoryId',
            'name',
            'cleanSetName',
            'urlName',
            'abbreviation',
            'releaseDate',
            'active'
        )