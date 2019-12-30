from django.shortcuts import render
from storage.models import Storage
from rest_framework import viewsets,generics
from storage.serializeres import *
from django.db.models import Q
# Create your views here.



class StorageView(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class ListStorageView(generics.ListCreateAPIView):
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

    def perform_create(self, serializer):
        print("data POST")
        # The request user is set as author automatically.
        # serializer.save(author=self.request.data)
        # print(self.request.data)
        data = self.request.data
        list_obj = []
        for i in data:
            obj_storage = Storage()
            obj_storage.key = i
            obj_storage.value = data[i]
            # print('key:',i ,'value:',data[i])
            list_obj.append(obj_storage)
        Storage.objects.bulk_create(list_obj)

    def perform_update(self, serializer):
        print('UPDATE')