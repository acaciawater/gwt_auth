from rest_framework import serializers

from gwt.models import SurveyData

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyData
        fields = '__all__'
