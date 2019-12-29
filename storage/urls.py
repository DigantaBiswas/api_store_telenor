from django.urls import include, path
from rest_framework import routers
from storage.views import StorageView,ListStorageView

router = routers.DefaultRouter()
# router.register(r'data', StorageView,basename = 'storage')
router.register('data', StorageView)


app_name = 'storage'
urlpatterns = [
    path('api/', include(router.urls)),
    path('', ListStorageView.as_view(),name="storage_filter"),

]