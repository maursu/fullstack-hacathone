from django.urls import path, include

from . import views

urlpatterns = [
    path('answer-reviews/', views.AnswerReviewListView.as_view()),
    path('question-reviews/', views.QuestionReviewListView.as_view()),
]
