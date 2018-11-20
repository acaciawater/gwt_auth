from rest_framework import serializers

from .models import SurveyData, Indicator, ClassLimit

class SurveySerializer(serializers.ModelSerializer):
#     user = SlugRelatedField(
#         slug_field='username',
#         queryset = User.objects.all()
#     )
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = SurveyData
        fields = ('user', 'project', 'location', 'survey')

class ClassLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLimit
        fields = ('limit', 'description')
        
class IndicatorSerializer(serializers.ModelSerializer):
    limits = ClassLimitSerializer(many=True)
    class Meta:
        model = Indicator
        fields = ('name','layer','url','limits')
