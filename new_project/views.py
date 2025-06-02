from django.shortcuts import render
from django.db.models.functions import Lower
from .serializers import WordSerializer
from rest_framework import viewsets , filters
from .models import Word


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering = ['name']
    search_fields = ['name']

    def get_queryset(self):
        queryset = self.queryset
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


    def get_queryset(self):
        return Word.objects.all().order_by(Lower('name'))

