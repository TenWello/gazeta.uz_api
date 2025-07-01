from django.urls import path, include
from .views import NewsListAPIView


urlpatterns = [
    path('gazeta-news/', NewsListAPIView.as_view(), name='gazeta-news'),
]