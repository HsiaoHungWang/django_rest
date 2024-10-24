from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Categories, Member, Spotimagesspot
from .serializers import CategorySerializers, MemberSerializers, SpotimagesspotSerializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

class SpotimagesspotPagination(PageNumberPagination):
    page_size=9 # 一頁幾筆資料
    page_size_query_param = 'page_size' # ?page_size=20
    def get_paginated_response(self, data):
        return Response({
            'total_page':self.page.paginator.num_pages,
            'current_page':self.page.number,
            'results': data
        })

class SpotimagesspotViewSet(viewsets.ModelViewSet):
    queryset = Spotimagesspot.objects.all()
    serializer_class = SpotimagesspotSerializers

    # 關鍵字搜尋 where spottitle like '%公園%'
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter ]
    search_fields = ['spottitle', 'spotdescription']

    # 過濾 where categoryid=1
    filterset_fields = ['categoryid']


    # 分頁功能
    pagination_class= SpotimagesspotPagination

