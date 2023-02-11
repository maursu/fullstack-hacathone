from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagListCreateView, QuestionView


router = DefaultRouter()
router.register('questions', QuestionView)

urlpatterns = [
    path('tags/', TagListCreateView.as_view()),
    path('', include(router.urls))
]