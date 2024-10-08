from rest_framework import serializers

class MergedCardSerializer(serializers.Serializer):
    types= serializers.JSONField()
    classes= serializers.JSONField()
    subtypes= serializers.JSONField()
    element= serializers.CharField(max_length=128)
    name= serializers.CharField(max_length=128)
    slug= serializers.CharField(max_length=128)
    effect= serializers.CharField(allow_null=True)
    rule= serializers.JSONField(allow_null=True)
    flavor= serializers.CharField(allow_null=True)
    cost_memory= serializers.IntegerField(allow_null=True)
    cost_reserve= serializers.IntegerField(allow_null=True)
    level= serializers.IntegerField(allow_null=True)
    power= serializers.IntegerField(allow_null=True)
    life= serializers.IntegerField(allow_null=True)
    durability= serializers.IntegerField(allow_null=True)
    speed= serializers.BooleanField(allow_null=True)
    legality= serializers.JSONField(allow_null=True)
    editions = serializers.JSONField(allow_null=True)

class FullDeckSerializer(serializers.Serializer):
    mat_deck= serializers.JSONField()
    main_deck= serializers.JSONField()
    side_deck= serializers.JSONField()