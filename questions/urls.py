from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('questions', views.QuestionViewSet)

urlpatterns = [
    path('tags/', views.TagListCreateView.as_view()),
    path('', include(router.urls))
]
