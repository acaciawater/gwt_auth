from django.contrib.gis.db import models as geo
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class SurveyData(geo.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('user')) 
    project = models.CharField(_('project name'),max_length=100)
    location = geo.GeometryField(_('location'),srid=4326)
    survey = fields.JSONField(_('survey'),default=dict,blank=True)
    objects = geo.Manager()
    created = models.DateTimeField(auto_now_add=True)    
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project
    
    class Meta:
        verbose_name = _('Survey')
        unique_together=('project','user')
            
class Indicator(models.Model):
    name = models.CharField(_('name'), max_length=100, unique=True)
    url = models.URLField(_('url'), max_length=255, default=settings.DEFAULT_WMS)
    layer = models.CharField(_('layer'), max_length=100)
    
    def __str__(self):
        return self.name
    
    def class_limits(self):
        return ','.join(map(str,self.limits.all()))

    class Meta:
        verbose_name = _('Indicator')
        ordering = ('name',)

class ClassLimit(models.Model):
    indicator = models.ForeignKey(Indicator,models.CASCADE,verbose_name=_('indicator'),related_name=_('limits'))
    limit = models.DecimalField(_('limit'), max_digits=10,decimal_places=3,blank=True, null=True)    
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return str(self.limit)

    class Meta:
        verbose_name = _('Class limit')
        ordering = ('limit',)

# class Question(models.Model):
#     question = models.CharField(_('question'),primary_key = True, max_length=100)
#     description = models.TextField(_('description'))
# 
#     def __str__(self):
#         return self.question
# 
#     class Meta:
#         verbose_name = _('question')
#         
#     
# class Rule(models.Model):
#     question = models.ForeignKey(Question, models.CASCADE,verbose_name=_('question'))
#     answer = models.CharField(_('answer'),max_length=100)
#     indicators = models.ManyToManyField(Indicator,verbose_name=_('indicators'))
#     
#     def indicator_list(self):
#         return ','.join(list(map(str,self.indicators.all())))
# 
#     def __str__(self):
#         return str(self.question)
# 
#     class Meta:
#         verbose_name = _('rule')
#         
    