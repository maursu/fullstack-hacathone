from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AnswerView


router = DefaultRouter()
router.register('questions', AnswerView)

urlpatterns = [
    path('', include(router.urls))
]
