from django.contrib import admin
from django.contrib.admin.decorators import register
from gwt.models import SurveyData, Indicator, ClassLimit

# Register your models here.
@register(SurveyData)
class SurveryDataAdmin(admin.ModelAdmin):
    model = SurveyData
    list_display = ('project','user','location')
    list_search = ('user',)

class ClassLimitInline(admin.TabularInline):
    model = ClassLimit
    list_display = ('limit','description')
    extra = 0
    
@register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    model = Indicator
    list_display = ('name','layer','class_limits','url')
    inlines = [ClassLimitInline]
    