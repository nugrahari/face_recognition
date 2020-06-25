from rest_framework import serializers
from .models import Dataset

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = (
        	'id', 
        	'url', 
        	'lbp_hist', 
        	'image', 
        	'label', 
        	'directory'
        )