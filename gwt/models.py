# from django.contrib.gis.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.utils.translation import gettext_lazy as _

class SurveyData(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('user')) 
    project = models.TextField(_('project name'),max_length=100,unique=True)
    # location = models.PointField(_('location'))
    survey = fields.JSONField(_('survey'))
        
