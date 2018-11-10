from django.contrib import admin
from django.contrib.admin.decorators import register
from gwt.models import SurveyData

# Register your models here.
@register(SurveyData)
class SurveryDataAdmin(admin.ModelAdmin):
    model = SurveyData
    list_display = ('project','user','location')
    list_search = ('user',)
