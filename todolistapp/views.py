import json
from django.shortcuts import render
from rest_framework import generics, response
from .serializers import *


def index(request):
    return render(request, 'todolist.html')


class Items(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers


class OneItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        Item.objects.get(id=kwargs.get('id')).delete()
        data = self.get_serializer(Item.objects.all(), many=True).data
        return response.Response({'data': data}, status=200)


class Clear(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

    def delete(self, request, *args, **kwargs):
        Item.objects.filter(done=True).delete()
        data = self.get_serializer(Item.objects.all(), many=True).data
        return response.Response({'data': data}, status=200)
