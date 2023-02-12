from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='MakersOverflow',
        description='StackOverflow for makers',
        default_version='v1'
    ), public= True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('api/v1/', include('questions.urls')),
    path('api/v1/', include('answers.urls')),
    path('api/v1/', include('reviews.urls')),
]
