from django.urls import path
from .views import ProjectListView, TagListView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('tag', TagListView.as_view()),
]
