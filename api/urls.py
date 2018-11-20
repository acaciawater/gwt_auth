from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import SurveyViewSet, IndicatorViewSet, MapViewSet, MapLayerViewSet

router = DefaultRouter()
router.register('survey', SurveyViewSet)
router.register('indicator', IndicatorViewSet)
router.register('map', MapViewSet)
router.register('layer', MapLayerViewSet)

schema_view = get_schema_view(title='GWT Authorization API')

urlpatterns = [
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='GWT Authorization API')),
    path('token/', obtain_jwt_token),
    path('token/refresh', refresh_jwt_token),
    path('token/verify', verify_jwt_token),
    path('', include(router.urls)),
]
