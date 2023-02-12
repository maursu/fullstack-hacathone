from django.contrib import admin

from .models import QuestionReview, AnswerReview

admin.site.register(QuestionReview)
admin.site.register(AnswerReview)
