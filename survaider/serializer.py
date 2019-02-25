from rest_framework import serializers
from . models import Adults,Adultdata


class AdultdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adultdata
        fields = '__all__'
