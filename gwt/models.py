from django.contrib.gis.db import models as geo
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

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
    info = models.URLField(_('info'),help_text=_('URL for background information'))
    
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
    
class Suggestion(models.Model):
    """Stores User submitted suggestions."""
    user = models.ForeignKey(User, models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

@receiver(post_save, sender=Suggestion)
def create_suggestion(sender, instance, created, **kwargs):
    """Upon Suggestion creation, send an email."""
    if created:
        send_mail(
            'Feedback by {}'.format(instance.user.username),
            instance.message,
            settings.EMAIL_HOST_USER,
            ['theo.kleinendorst@acaciawater.com'],
            fail_silently=False,
        )
