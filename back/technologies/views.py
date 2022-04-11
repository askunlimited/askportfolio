from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import Technology
from .serializers import TechnologySerializer


class TechnologyListView(ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
