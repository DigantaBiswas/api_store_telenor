from django.shortcuts import render
from storage.models import Storage
from rest_framework import viewsets,generics
from storage.serializeres import *
from django.db.models import Q
# Create your views here.



class StorageView(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class ListStorageView(generics.ListAPIView):
    serializer_class = StorageSerializer

    def get_queryset(self):
        qs = Storage.objects.all()
        query = self.request.query_params.get("keys")
        try:
            query = query.split(",")
            if query is not None:
                print(query)
                qs = qs.filter(key__in = query)

            return qs
        except:
            return qs