from rest_framework import serializers

from .models import SurveyData, Indicator, ClassLimit, Suggestion

class SurveySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = SurveyData
        fields = ('user', 'project', 'location', 'survey', 'created', 'modified')

class ClassLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLimit
        fields = ('limit', 'description')
        
class IndicatorSerializer(serializers.ModelSerializer):
    limits = ClassLimitSerializer(many=True)
    class Meta:
        model = Indicator
        fields = ('name','layer','url','limits','info')

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('user', 'created', 'message')
            