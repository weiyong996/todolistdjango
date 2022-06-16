import logging

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics

from todolist.serializers import ItemSerializer
from todolist.models import Item


class ItemListView(generics.ListCreateAPIView):
    """
    获取所有Item
    创建1个新Item
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    检索、更新或删除一个Item
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
