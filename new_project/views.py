from django.db.models.functions import Lower
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Word
from .serializers import WordSerializer


@api_view(['GET'])
def word_list(request):
    words = Word.objects.all().order_by(Lower('name'))

    name = request.query_params.get('name')
    if name:
        words = words.filter(name__icontains=name)

    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(words, request)
    serializer = WordSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def word_detail(request, pk):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return Response({'error': 'Word not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def word_create(request):
    serializer = WordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
