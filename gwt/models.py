from django.contrib.gis.db import models
#from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.utils.translation import gettext_lazy as _

class SurveyData(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('user')) 
    project = models.CharField(_('project name'),max_length=100,unique=True)
    location = models.GeometryField(_('location'),srid=4326)
    survey = fields.JSONField(_('survey'),default=dict,blank=True)

    def __str__(self):
        return self.project
        
