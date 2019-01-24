from django.contrib import admin
from django.contrib.admin.decorators import register
from gwt.models import SurveyData, Indicator, ClassLimit#, Question, Rule

# Register your models here.
@register(SurveyData)
class SurveryDataAdmin(admin.ModelAdmin):
    model = SurveyData
    list_display = ('project','user','location','created','modified')
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

# @register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     model = Question
#     list_display=('question','description')
#     
# @register(Rule)
# class RuleAdmin(admin.ModelAdmin):
#     model = Rule
#     list_display = ('question','answer','indicator_list')