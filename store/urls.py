from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from pprint import pprint

# router = SimpleRouter()
router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

# Url Conf
# urlpatterns = [
#     path('', include(router.urls))
# ]
urlpatterns = router.urls