import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from todolist.serializers import ItemSerializer
from todolist.models import Item


class ItemListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)



