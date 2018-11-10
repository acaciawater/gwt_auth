from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import SurveyViewSet

router = DefaultRouter()
router.register('survey', SurveyViewSet)

schema_view = get_schema_view(title='GWT Authorization API')

urlpatterns = [
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='GWT Authorization API')),
    path('login/', obtain_jwt_token),
    path('', include(router.urls)),
]
