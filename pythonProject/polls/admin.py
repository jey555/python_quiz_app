from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

    # change the order of the fields


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
