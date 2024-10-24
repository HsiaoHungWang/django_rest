from django.shortcuts import render
from rest_framework import viewsets
from .models import Categories, Member, Spotimagesspot
from .serializers import CategorySerializers, MemberSerializers, SpotimagesspotSerializers

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

class SpotimagesspotViewSet(viewsets.ModelViewSet):
    queryset = Spotimagesspot.objects.all()
    serializer_class = SpotimagesspotSerializers

