from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all().order_by("id")
    serializer_class = SubjectSerializer
    filter_backends = [
        SearchFilter,
    ]
    pagination_class = PageNumberPagination
    search_fields = ["name"]
