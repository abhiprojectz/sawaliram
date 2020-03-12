from django.contrib import admin
from .models import (
    Question,
    Answer,
    Article,
    AnswerCredit,
)

class AnswerCreditInline(admin.TabularInline):
    model = AnswerCredit
    view_on_site = False
    show_change_link = True

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    def question_text_english(obj):
        return (obj.question_id.question_text_english
            or obj.question_id.question_text)
    question_text_english.short_description = 'Question (en)'
    list_display = [
        'question_id',
        question_text_english,
        'status',
        'submitted_by',
        'created_on',
        'updated_on',
    ]
    fields = [
        'question_id',
        'language',
        'answer_text',
        'status',
        'submitted_by',
        'approved_by',
    ]
    search_fields = ['question_id__id', 'question_id__question_text']
    inlines = [
        AnswerCreditInline,
    ]
    date_hierarchy = 'created_on'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['id', 'question_text', 'question_text_english']
    list_filter = ['language', 'state', 'field_of_interest']
    list_display = ['id', 'question_text', 'question_text_english', 'field_of_interest', 'area', 'state']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_filter = ['language', 'author']
    list_display = ['id', 'title', 'body', 'created_on', 'updated_on', 'published_on','author']
    date_hierarchy = 'published_on'
