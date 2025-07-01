from rest_framework.generics import ListAPIView
from .models import News
from .serializers import NewsItemSerializer

class NewsListAPIView(ListAPIView):
    queryset = News.objects.order_by('-id')
    serializer_class = NewsItemSerializer