from rest_framework import serializers
from myproduct.models import Myproduct

class MyproductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Myproduct
        fields= ["id","name","sector","price","description"]
