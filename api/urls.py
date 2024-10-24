from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# https://..../category
router.register('category', views.CategoryViewSet)
# https://..../member
router.register('member', views.MemberViewSet)
# https://..../spots
router.register('spots', views.SpotimagesspotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]