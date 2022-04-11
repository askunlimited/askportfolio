from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import Project, Tag
from .serializers import ProjectSerializer, TagSerializer


class ProjectListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = None



class TagListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
