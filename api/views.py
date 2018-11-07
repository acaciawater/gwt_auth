from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import SurveySerializer
from gwt.models import SurveyData

class SurveyViewSet(ModelViewSet):
    """ 
    This view a describes a list of surveys and allows new surveys to be created
    """    
    serializer_class = SurveySerializer
    queryset = SurveyData.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        return user.surveydata_set.all()