from django.shortcuts import render
from rest_framework import viewsets
from .models import Categories, Member
from .serializers import CategorySerializers, MemberSerializers

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

