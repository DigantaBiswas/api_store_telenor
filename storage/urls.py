from django.urls import include, path
from rest_framework import routers
from storage.views import StorageView

router = routers.DefaultRouter()
router.register(r'data', StorageView)


app_name = 'storage'
urlpatterns = [
    path('api/', include(router.urls))
]