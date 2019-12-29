from django.shortcuts import render
from storage.models import Storage
from rest_framework import viewsets
from storage.serializeres import *

# Create your views here.
class StorageView(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


# class ActuatorListApiView(generics.ListAPIView):
#     serializer_class = ActuatorSerializer
#
#     def get_queryset(self):
#         qs = Actuator.objects.all()
#         query = self.request.GET.get("q")
#
#         if query is not None:
#             qs = qs.filter(
#                 Q(topic__icontains=query)
#             ).distinct().order_by('-time')[:1]
#
#         return qs