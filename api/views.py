from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated,\
    IsAuthenticatedOrReadOnly

from gwt.models import SurveyData, Indicator
from gwt.serializers import SurveySerializer, IndicatorSerializer

from wms.models import Map, MapLayer
from wms.serializers import MapLayerSerializer, MapSerializer
from rest_framework_filters.backends import DjangoFilterBackend

class SurveyViewSet(ModelViewSet):
    """ 
    This view a describes a list of surveys and allows new surveys to be created
    """    
    serializer_class = SurveySerializer
    queryset = SurveyData.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_fields = ('project',)
    
    def get_queryset(self):
        """ 
        Returns the surveys of authenticated user 
        """
        user = self.request.user
        return user.surveydata_set.all()
    
class IndicatorViewSet(ReadOnlyModelViewSet):
    """ 
    This view a describes a list of indicators
    """    
    serializer_class = IndicatorSerializer
    queryset = Indicator.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', )
    permission_classes = (IsAuthenticatedOrReadOnly,)

class MapViewSet(ReadOnlyModelViewSet):
    """ 
    This view a describes a list of maps
    """    
    serializer_class = MapSerializer
    queryset = Map.objects.all()
    filter_fields = ('name', )
    
class MapLayerViewSet(ReadOnlyModelViewSet):
    """ 
    This view a describes a list of layers
    """    
    serializer_class = MapLayerSerializer
    queryset = MapLayer.objects.all()

    
        