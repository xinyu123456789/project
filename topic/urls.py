from django.urls import path
from .views import *

urlpatterns = [
    path('', TopicList.as_view(), name='topic_list'),
    path('', TopicSearch.as_view(), name='topic_search'),
    path('new/', TopicNew.as_view(), name='topic_new'), 
    path('<int:pk>/', TopicView.as_view(), name='topic_view'),
    path('<int:pk>/delete/', TopicDelete.as_view(), name='topic_delete'),
]